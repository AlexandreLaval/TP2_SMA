import random

from pygame import Vector2

from Agent import Agent
from CarnivoreBody import CarnivoreBody
from VegetalItem import VegetalItem


class HerbivoreAgent(Agent):
    def __init__(self, body):
        super().__init__(body)

    def doMange(self, proie):
        if isinstance(proie, VegetalItem):
            return True

    def update(self):
        super().update()
    #     if not self.body.isDead:
    #         proies, predateurs = self.filterPerception()
    #         cible = None
    #         distanceCible = 10000
    #
    #         for p in proies:
    #             if p.position.distance_to(self.body.position) < distanceCible:
    #                 cible = p
    #                 distanceCible = p.position.distance_to(self.body.position)
    #
    #         if cible is not None:
    #             force = cible.position - self.body.position
    #             self.acceleration = force
    #         else:
    #             self.acceleration = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
    #
    #         if self.acceleration.length() > self.body.maxAcc:
    #             self.acceleration.scale_to_length(self.body.maxAcc)
    #
    #         self.vitesse = self.body.velocity + self.acceleration
    #
    #         if self.vitesse.length() > self.body.maxSpeed:
    #             self.vitesse.scale_to_length(self.body.maxSpeed)
    #
    #         self.body.position = self.body.position + self.vitesse
    #
    #         self.acceleration = Vector2(0, 0)

    def filterPerception(self):
        proies = []
        predateurs = []
        for i in self.body.fustrum.perceptionList:
            if type(i).__name__ == "VegetalItem":
                proies.append(i)
            if type(i).__name__ == "CarnivoreBody":
                if not i.isDead:
                    predateurs.append(i)
        return proies, predateurs
