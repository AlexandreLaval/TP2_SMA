import random

from pygame import Vector2

import core
from Body import Body
from Fustrum import Fustrum
from Jauge import Jauge


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
        self.esperance = random.randint(core.memory("scenario")['Carnivore']['parametres']['MaxEsperance'][0],
                                        core.memory("scenario")['Carnivore']['parametres']['MaxEsperance'][1])

    def show(self):
        if not self.isDead:
            core.Draw.circle(self.color, self.position, self.bodySize)
        else:
            pass
            core.Draw.circle((211, 211, 211), self.position, self.bodySize)

    def reproduction(self):
        from CarnivoreAgent import CarnivoreAgent
        c = CarnivoreAgent(CarnivoreBody(self.position + Vector2(random.randint(-1, 1), random.randint(-1, 1))))
        core.memory('agents').append(c)
