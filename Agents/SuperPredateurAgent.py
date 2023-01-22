import random

from pygame import Vector2

from Agents.Agent import Agent
from Bodies.CarnivoreBody import CarnivoreBody
from Bodies.Fustrum import Fustrum


class SuperPredateurAgent(Agent):
    def __init__(self, body):
        super().__init__(body)
        self.fustrum = Fustrum(130, self)

    def doMange(self, proie):
        if hasattr(proie, 'body'):
            if isinstance(proie.body, CarnivoreBody):
                return True

    def update(self):
        preys = self.filterPerception()
        self.computeForce(preys)

    def computeForce(self, preys):
        hunt = self.hunt(preys) * 1

        if  hunt == (0, 0):
            target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
            while target.length() == 0:
                target = Vector2(random.randint(-1, 1), random.randint(-1, 1))

            target.scale_to_length(target.length())
            self.body.acceleration += target
        else:
            self.body.acceleration += hunt

    def filterPerception(self):
        proies = []
        for i in self.body.fustrum.perceptionList:
            if isinstance(i, CarnivoreBody):
                if not i.isDead:
                    proies.append(i)
        return proies


    def hunt(self, preys):
        steering = Vector2()
        if len(preys) > 0:
            prey = sorted(preys, key=lambda x: x.position.distance_to(self.body.position), reverse=True)[0]
            steering = prey.position - self.body.position
        return steering
