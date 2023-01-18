import random

from pygame import Vector2

import core
from Fustrum import Fustrum
from HerbivoreAgent import HerbivoreAgent
from Body import Body
from Jauge import Jauge


class HerbivoreBody(Body):
    def __init__(self, pos = None):
        super().__init__(pos)
        self.color = (0, 255, 0)
        self.jaugeFaim = Jauge(random.randint(core.memory("scenario")['Herbivore']['parametres']['MaxFaim'][0],
                                              core.memory("scenario")['Herbivore']['parametres']['MaxFaim'][1]),
                               1)
        self.jaugeFatigue = Jauge(random.randint(core.memory("scenario")['Herbivore']['parametres']['MaxFatigue'][0],
                                                 core.memory("scenario")['Herbivore']['parametres']['MaxFatigue'][1]),
                                  1)
        self.jaugeReproduction = Jauge(
            random.randint(core.memory("scenario")['Herbivore']['parametres']['MaxReproduction'][0],
                           core.memory("scenario")['Herbivore']['parametres']['MaxReproduction'][1]),
            1)
        self.maxAcc = random.randint(core.memory("scenario")['Herbivore']['parametres']['accelerationMax'][0],
                                     core.memory("scenario")['Herbivore']['parametres']['accelerationMax'][1])
        self.maxSpeed = random.randint(core.memory("scenario")['Herbivore']['parametres']['vitesseMax'][0],
                                       core.memory("scenario")['Herbivore']['parametres']['vitesseMax'][1])
        self.esperance = random.randint(core.memory("scenario")['Herbivore']['parametres']['MaxEsperance'][0],
                                        core.memory("scenario")['Herbivore']['parametres']['MaxEsperance'][1])

    def show(self):
        if not self.isDead:
            core.Draw.circle(self.color, self.position, self.bodySize)
        else:
            core.Draw.circle((211, 211, 211), self.position, self.bodySize)


    def reproduction(self):
        core.memory('agents').append(
            HerbivoreAgent(HerbivoreBody(self.position+Vector2(random.randint(-1, 1), random.randint(-1, 1)))))
