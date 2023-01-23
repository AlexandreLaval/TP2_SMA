import random

from pygame import Vector2

import core
from Agents.HerbivoreAgent import HerbivoreAgent
from Bodies.Body import Body
from Bodies.Fustrum import Fustrum
from Bodies.Jauge import Jauge


class HerbivoreBody(Body):
    def __init__(self, pos=None):
        super().__init__(pos)
        self.fustrum = Fustrum(110, self)
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
        self.esperance = random.randint(core.memory("scenario")['Herbivore']['parametres']['esperance'][0],
                                        core.memory("scenario")['Herbivore']['parametres']['esperance'][1])

    def show(self):
        if not self.isDead:
            if self.isSleeping:
                core.Draw.text(self.color, "Dodo", Vector2(self.position.x - 10, self.position.y - 30), taille=15)
            core.Draw.circle(self.color, self.position, self.bodySize)
        else:
            core.Draw.circle((211, 211, 211), self.position, self.bodySize)

    def reproduction(self):
        core.memory('agents').append(
            HerbivoreAgent(HerbivoreBody(self.position + Vector2(random.randint(-1, 1), random.randint(-1, 1)))))
