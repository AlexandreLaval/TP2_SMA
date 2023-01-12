import random

from pygame import Vector2

from Agent import Agent
from HerbivoreBody import HerbivoreBody
from SuperPredateurBody import SuperPredateurBody


class CarnivoreAgent(Agent):
    def __init__(self, body):
        super().__init__(body)

    def update(self):
        if not self.body.isDead:
            preys, predateurs = self.filterPerception()
            self.computeForce(preys, predateurs)
    def filterPerception(self):
        proies = []
        predateurs = []
        for i in self.body.fustrum.perceptionList:
            if type(i).__name__ == HerbivoreBody.__class__.__name__:
                if not i.isDead:
                    proies.append(i)
            if type(i).__name__ == SuperPredateurBody.__class__.__name__:
                if not i.isDead:
                    predateurs.append(i)
        return proies, predateurs


    def manger(self, proies):
        proiesDansVision = []
        cible = None
        distanceCible = 10000

        for p in proies:
            if p.position.distance_to(self.position)<self.vision and p.vivante:
                proiesDansVision.append(p)
                if p.position.distance_to(self.position) < distanceCible :
                    cible = p
                    distanceCible = p.position.distance_to(self.position)

        if cible is not None:
            force = cible.position - self.position
            self.acceleration = force
        else:
            self.acceleration = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

