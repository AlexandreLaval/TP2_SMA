import random

from pygame import Vector2

import core
from Bodies.Body import Body
from Bodies.Fustrum import Fustrum
from Bodies.Jauge import Jauge


class CarnivoreBody(Body):
    def __init__(self, pos=None):
        super().__init__(pos)
        self.fustrum = Fustrum(120, self)
        self.color = (255, 0, 0)
        self.bodySize = 10
        self.jaugeFaim = Jauge(random.randint(core.memory("scenario")['Carnivore']['parametres']['MaxFaim'][0],
                                              core.memory("scenario")['Carnivore']['parametres']['MaxFaim'][1]),
                               1)
        self.jaugeFatigue = Jauge(random.randint(core.memory("scenario")['Carnivore']['parametres']['MaxFatigue'][0],
                                                 core.memory("scenario")['Carnivore']['parametres']['MaxFatigue'][1]),
                                  1)
        self.jaugeReproduction = Jauge(
            random.randint(core.memory("scenario")['Carnivore']['parametres']['MaxReproduction'][0],
                           core.memory("scenario")['Carnivore']['parametres']['MaxReproduction'][1]),
            1)
        self.maxAcc = random.randint(core.memory("scenario")['Carnivore']['parametres']['accelerationMax'][0],
                                     core.memory("scenario")['Carnivore']['parametres']['accelerationMax'][1])
        self.maxSpeed = random.randint(core.memory("scenario")['Carnivore']['parametres']['vitesseMax'][0],
                                       core.memory("scenario")['Carnivore']['parametres']['vitesseMax'][1])
        self.esperance = random.randint(core.memory("scenario")['Carnivore']['parametres']['esperance'][0],
                                        core.memory("scenario")['Carnivore']['parametres']['esperance'][1])

    def show(self):
        if not self.isDead:
            if self.isSleeping:
                core.Draw.text(self.color, "Dodo", Vector2(self.position.x - 10, self.position.y - 30), taille=15)
            core.Draw.circle(self.color, self.position, self.bodySize)
        else:
            core.Draw.circle((211, 211, 211), self.position, self.bodySize)

    def reproduction(self):
        from Agents.CarnivoreAgent import CarnivoreAgent
        c = CarnivoreAgent(CarnivoreBody(self.position + Vector2(random.randint(-1, 1), random.randint(-1, 1))))
        core.memory('agents').append(c)


