import random

from pygame import Vector2

import core
from DecomposeurAgent import DecomposeurAgent
from Body import Body
from Jauge import Jauge
from PersonalRandom import PersonalRandom


class DecomposeurBody(Body):
    def __init__(self, JaugeFaim, JaugeFatigue, JaugeReproduction, pos=None):
        super().__init__(JaugeFaim, JaugeFatigue, JaugeReproduction, pos)
        self.color = (88, 41, 0)

    def show(self):
        if not self.isDead:
            core.Draw.circle(self.color, self.position, self.bodySize)
        else:
            core.Draw.circle((211,211,211), self.position, self.bodySize)

    def reproduction(self):
        core.memory('agents').append(
            DecomposeurAgent(DecomposeurBody(PersonalRandom.randomJaugeFaim(PersonalRandom()),
                                         PersonalRandom.randomJaugeFatigue(PersonalRandom()),
                                         PersonalRandom.randomJaugeReproduction(PersonalRandom()),
                                         self.position+Vector2(random.randint(-1, 1), random.randint(-1, 1)))))
