import random

from pygame import Vector2

import core
from HerbivoreAgent import HerbivoreAgent
from Body import Body
from Jauge import Jauge


class HerbivoreBody(Body):
    def __init__(self, JaugeFaim, JaugeFatigue, JaugeReproduction, pos = None):
        super().__init__(JaugeFaim, JaugeFatigue, JaugeReproduction, pos)
        self.color = (0, 255, 0)

    def show(self):
        if not self.isDead:
            core.Draw.circle(self.color, self.position, self.bodySize)
        else:
            core.Draw.circle((211, 211, 211), self.position, self.bodySize)


    def reproduction(self):
        core.memory('agents').append(
            HerbivoreAgent(HerbivoreBody(Jauge(0, 10, 1), Jauge(0, 10, 1), Jauge(0, 10, 1),
                                         self.position + Vector2(random.randint(-1, 1), random.randint(-1, 1)))))
