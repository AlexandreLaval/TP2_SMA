import random

from pygame import Vector2

from Agents.Agent import Agent
from Bodies.CarnivoreBody import CarnivoreBody
from Bodies.SuperPredateurBody import SuperPredateurBody
from Items.VegetalItem import VegetalItem


class HerbivoreAgent(Agent):
    def __init__(self, body):
        super().__init__(body)

    def doMange(self, proie):
        if isinstance(proie, VegetalItem):
            return True

    def update(self):
        preys, predators, symbiotics = self.filterPerception()
        self.computeForce(preys, predators, symbiotics)

    def computeForce(self, preys, predators, symbiotics):
        flee = self.flee(predators) * 2
        hunt = self.hunt(preys) * 1.5
        if len(predators) > 0:
            symbiose = self.symbiosis(symbiotics) * 1
        else:
            symbiose = (0, 0)

        if flee + hunt + symbiose == (0, 0):
            target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
            while target.length() == 0:
                target = Vector2(random.randint(-1, 1), random.randint(-1, 1))

            target.scale_to_length(target.length())
            self.body.acceleration += target
        else:
            self.body.acceleration += hunt + flee + symbiose

    def filterPerception(self):
        preys = []
        predateurs = []
        symbiotics = []
        for i in self.body.fustrum.perceptionList:
            if isinstance(i, VegetalItem):
                preys.append(i)
            if isinstance(i, CarnivoreBody):
                if not i.isDead:
                    predateurs.append(i)
            if isinstance(i, SuperPredateurBody):
                if not i.isDead:
                    symbiotics.append(i)
        return preys, predateurs, symbiotics

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

    def flee(self, predators):
        force = Vector2()
        if len(predators) > 0:
            prey = sorted(predators, key=lambda x: x.position.distance_to(self.body.position), reverse=True)[0]
            force = prey.position + self.body.position
        return force

    def symbiosis(self, symbiotics):
        force = Vector2()
        if len(symbiotics) > 0:
            prey = sorted(symbiotics, key=lambda x: x.position.distance_to(self.body.position), reverse=True)[0]
            force = prey.position - self.body.position
        return force
