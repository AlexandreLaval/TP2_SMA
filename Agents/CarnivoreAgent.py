import random

from pygame import Vector2

from Agents.Agent import Agent
from Bodies.HerbivoreBody import HerbivoreBody
from Bodies.SuperPredateurBody import SuperPredateurBody


class CarnivoreAgent(Agent):
    def __init__(self, body):
        super().__init__(body)

    def doMange(self, proie):
        if hasattr(proie, 'body'):
            if isinstance(proie.body, HerbivoreBody):
                return True

    def update(self):
        preys, predators = self.filterPerception()
        self.computeForce(preys, predators)

    def computeForce(self, preys, predators):
        flee = self.flee(predators) * 2
        hunt = self.hunt(preys) * 1

        if flee + hunt == (0, 0):
            target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
            while target.length() == 0:
                target = Vector2(random.randint(-1, 1), random.randint(-1, 1))

            target.scale_to_length(target.length())
            self.body.acceleration += target
        else:
            self.body.acceleration += hunt + flee

    def filterPerception(self):
        preys = []
        predateurs = []
        for i in self.body.fustrum.perceptionList:
            if isinstance(i, HerbivoreBody):
                if not i.isDead:
                    preys.append(i)
            if isinstance(i, SuperPredateurBody):
                if not i.isDead:
                    predateurs.append(i)
        return preys, predateurs

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
