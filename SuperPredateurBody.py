import random

from pygame import Vector2

import core
from PersonalRandom import PersonalRandom
from SuperPredateurAgent import SuperPredateurAgent
from Body import Body
from Jauge import Jauge


class SuperPredateurBody(Body):
    def __init__(self, JaugeFaim, JaugeFatigue, JaugeReproduction, pos = None):
        super().__init__(JaugeFaim, JaugeFatigue, JaugeReproduction, pos)
        self.color = (0, 0, 255)
        self.bodySize = 14

    def show(self):
        if not self.isDead:
            core.Draw.circle(self.color, self.position, self.bodySize)
        else:
            core.Draw.circle((211, 211, 211), self.position, self.bodySize)
    def reproduction(self):
        core.memory('agents').append(
            SuperPredateurAgent(SuperPredateurBody(PersonalRandom.randomJaugeFaim(PersonalRandom()),
                                         PersonalRandom.randomJaugeFatigue(PersonalRandom()),
                                         PersonalRandom.randomJaugeReproduction(PersonalRandom()),
                                         self.position+Vector2(random.randint(-1, 1), random.randint(-1, 1)))))