import random

from pygame import Vector2

from Agents.Agent import Agent
from Bodies.Fustrum import Fustrum


class DecomposeurAgent(Agent):
    def __init__(self, body):
        super().__init__(body)
        self.fustrum = Fustrum(200, self)

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
            self.body.acceleration += Vector2(random.randint(-5, 5), random.randint(-5, 5))
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
        steering = Vector2()
        if len(preys) > 0:
            prey = sorted(preys, key=lambda x: x.position.distance_to(self.body.position), reverse=True)[0]
            steering = prey.position - self.body.position
        return steering
