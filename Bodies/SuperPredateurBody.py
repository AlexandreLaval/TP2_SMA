import random

from pygame import Vector2

import core

from Agents.SuperPredateurAgent import SuperPredateurAgent
from Bodies.Body import Body
from Bodies.Jauge import Jauge


class SuperPredateurBody(Body):
    def __init__(self, pos = None):
        super().__init__(pos)
        self.color = (0, 0, 255)
        self.bodySize = 14
        self.jaugeFaim = Jauge(random.randint(core.memory("scenario")['SuperPredateur']['parametres']['MaxFaim'][0],
                                              core.memory("scenario")['SuperPredateur']['parametres']['MaxFaim'][1]),
                               1)
        self.jaugeFatigue = Jauge(random.randint(core.memory("scenario")['SuperPredateur']['parametres']['MaxFatigue'][0],
                                                 core.memory("scenario")['SuperPredateur']['parametres']['MaxFatigue'][1]),
                                  1)
        self.jaugeReproduction = Jauge(
            random.randint(core.memory("scenario")['SuperPredateur']['parametres']['MaxReproduction'][0],
                           core.memory("scenario")['SuperPredateur']['parametres']['MaxReproduction'][1]),
            1)
        self.maxAcc = random.randint(core.memory("scenario")['SuperPredateur']['parametres']['accelerationMax'][0],
                                     core.memory("scenario")['SuperPredateur']['parametres']['accelerationMax'][1])
        self.maxSpeed = random.randint(core.memory("scenario")['SuperPredateur']['parametres']['vitesseMax'][0],
                                       core.memory("scenario")['SuperPredateur']['parametres']['vitesseMax'][1])
        self.esperance = random.randint(core.memory("scenario")['SuperPredateur']['parametres']['MaxEsperance'][0],
                                        core.memory("scenario")['SuperPredateur']['parametres']['MaxEsperance'][1])

    def show(self):
        if not self.isDead:
            if self.isSleeping:
                core.Draw.text(self.color, "Dodo", Vector2(self.position.x - 10, self.position.y - 30), taille=15)
            core.Draw.circle(self.color, self.position, self.bodySize)
        else:
            core.Draw.circle((211, 211, 211), self.position, self.bodySize)
    def reproduction(self):
        core.memory('agents').append(
            SuperPredateurAgent(SuperPredateurBody(self.position+Vector2(random.randint(-1, 1), random.randint(-1, 1)))))