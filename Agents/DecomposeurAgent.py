import random

from pygame import Vector2

from Agents.Agent import Agent
from Bodies.Fustrum import Fustrum


class DecomposeurAgent(Agent):
    def __init__(self, body):
        super().__init__(body)
        self.fustrum = Fustrum(500, self)

    def doMange(self, proie):
        if(hasattr(proie, 'body')):
            if hasattr(proie.body, 'isDead'):
                if proie.body.isDead:
                    return True
    #
    def update(self):
        preys = self.filterPerception()
        self.computeForce(preys)

        # if len(preys) == 0:
        #     if len(predators) == 0:
        #         target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
        #         while target.length() == 0:
        #             target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
        #
        #         target.scale_to_length(target.length())
        #         self.body.acceleration += target

    def computeForce(self, preys):
        hunt = self.hunt(preys) * 1

        if hunt == (0, 0):
            target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
            while target.length() == 0:
                target = Vector2(random.randint(-1, 1), random.randint(-1, 1))

            target.scale_to_length(target.length())
            self.body.acceleration += target
        else:
            self.body.acceleration += hunt

    def filterPerception(self):
        preys = []
        for i in self.body.fustrum.perceptionList:
            if hasattr(i, 'isDead'):
                if i.isDead:
                    preys.append(i)
        return preys


    def hunt(self, preys):
        cible = None
        distanceCible = 10000
        force = Vector2()
        for p in preys:
            if p.position.distance_to(self.body.position) < distanceCible:
                cible = p
                distanceCible = p.position.distance_to(self.body.position)

        if cible is not None:
            force = cible.position - self.body.position
        return force
