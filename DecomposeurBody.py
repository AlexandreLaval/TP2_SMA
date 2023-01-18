import random

from pygame import Vector2

import core
from DecomposeurAgent import DecomposeurAgent
from Body import Body
from Jauge import Jauge


class DecomposeurBody(Body):
    def __init__(self, pos=None):
        super().__init__(pos)
        self.color = (88, 41, 0)
        self.jaugeFaim = Jauge(random.randint(core.memory("scenario")['Decomposeur']['parametres']['MaxFaim'][0],
                                              core.memory("scenario")['Decomposeur']['parametres']['MaxFaim'][1]),
                               1)
        self.jaugeFatigue = Jauge(random.randint(core.memory("scenario")['Decomposeur']['parametres']['MaxFatigue'][0],
                                                 core.memory("scenario")['Decomposeur']['parametres']['MaxFatigue'][1]),
                                  1)
        self.jaugeReproduction = Jauge(
            random.randint(core.memory("scenario")['Decomposeur']['parametres']['MaxReproduction'][0],
                           core.memory("scenario")['Decomposeur']['parametres']['MaxReproduction'][1]),
            1)
        self.maxAcc = random.randint(core.memory("scenario")['Decomposeur']['parametres']['accelerationMax'][0],
                                     core.memory("scenario")['Decomposeur']['parametres']['accelerationMax'][1])
        self.maxSpeed = random.randint(core.memory("scenario")['Decomposeur']['parametres']['vitesseMax'][0],
                                       core.memory("scenario")['Decomposeur']['parametres']['vitesseMax'][1])
        self.esperance = random.randint(core.memory("scenario")['Decomposeur']['parametres']['MaxEsperance'][0],
                                        core.memory("scenario")['Decomposeur']['parametres']['MaxEsperance'][1])

    def show(self):
        if not self.isDead:
            core.Draw.circle(self.color, self.position, self.bodySize)
        else:
            core.Draw.circle((211,211,211), self.position, self.bodySize)

    def reproduction(self):
        core.memory('agents').append(
            DecomposeurAgent(DecomposeurBody(self.position+Vector2(random.randint(-1, 1), random.randint(-1, 1)))))
