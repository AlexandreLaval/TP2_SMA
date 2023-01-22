import random

from pygame import Vector2

from Agents.Agent import Agent
from Bodies.CarnivoreBody import CarnivoreBody
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
            symbiosis = self.symbiosis(symbiotics) * 1
        else:
            symbiosis = (0,0)

        if flee + hunt + symbiosis == (0, 0):
            self.body.acceleration += Vector2(random.randint(-5, 5), random.randint(-5, 5))
        else:
            self.body.acceleration += hunt + flee

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
            if isinstance(i, self.body.__class__):
                if not i.isDead:
                    symbiotics.append(i)
        return preys, predateurs, symbiotics


    def hunt(self, preys):
        steering = Vector2()
        if len(preys) > 0:
            prey = sorted(preys, key=lambda x: x.position.distance_to(self.body.position), reverse=True)[0]
            steering = prey.position - self.body.position
        return steering

    def flee(self, predators):
        steering = Vector2()
        if len(predators) > 0:
            prey = sorted(predators, key=lambda x: x.position.distance_to(self.body.position), reverse=True)[0]
            steering = prey.position + self.body.position
        return steering

    def symbiosis(self, symbiotics):
        steering = Vector2()
        if len(symbiotics) > 0:
            prey = sorted(symbiotics, key=lambda x: x.position.distance_to(self.body.position), reverse=True)[0]
            steering = prey.position - self.body.position
        return steering