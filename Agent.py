import random

from pygame import Vector2


class Agent(object):
    def __init__(self, body):
        self.body = body
        self.uuid = random.randint(100000, 999999999)

    def mangeur(self, proies):
        pass

    def survie(self, predateur):
        pass

    def symbiose(self, symbiote):
        pass

    def wantToEat(self):
        if self.body.jaugeFaim.value > self.body.jaugeFaim.max / 2:
            return True

    def filterPerception(self):
        preys = []
        predators = []
        return preys, predators

    def update(self):
        preys, predators = self.filterPerception()
        self.computeForce(preys, predators)

        if len(preys) == 0:
            if len(predators) == 0:
                target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
                while target.length() == 0:
                    target = Vector2(random.randint(-1, 1), random.randint(-1, 1))

                target.scale_to_length(target.length())
                self.body.acceleration += target

    def computeForce(self, preys, predators):
        preysList = []
        for p in preys:
            if p.position.distance_to(self.body.position) < self.body.fustrum.radius:
                preysList.append(p)
        predatorsList = []
        for p in predators:
            if p.position.distance_to(self.body.position) < self.body.fustrum.radius:
                predatorsList.append(p)

        cible = None
        distanceCible = 10000
        for p in preysList:
            if p.position.distance_to(self.body.position) < distanceCible:
                cible = p
                distanceCible = p.position.distance_to(self.body.position)

        if len(predators) > 0:
            f = self.fear(predatorsList)
            self.body.acceleration = self.body.acceleration - f
        elif cible is not None:
            force = cible.position - self.body.position
            self.body.acceleration = force


    def fear(self, predators):
        steering = Vector2()
        predatorCounter = 0
        for other in predators:
            if self.body.position.distance_to(other.position) != 0:
                diff = Vector2(other.position.x - self.body.position.x, other.position.y - self.body.position.y)
                if diff.length() > 0.001:
                    diff.scale_to_length(self.body.position.distance_squared_to(other.position))
                    predatorCounter += 1
                    steering += diff
            else:
                steering += Vector2(random.uniform(-5, 5), random.uniform(-5, 5))
                predatorCounter += 1

        if predatorCounter > 0:
            steering /= predatorCounter

            steering += self.body.velocity

            if steering.length() > self.body.maxAcc:
                steering = steering.normalize()
                steering.scale_to_length(self.body.maxAcc)
        return steering

    def show(self):
        self.body.show()
