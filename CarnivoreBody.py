import random

from pygame import Vector2


import core
from Body import Body
from Jauge import Jauge
from PersonalRandom import PersonalRandom


class CarnivoreBody(Body):
    def __init__(self, JaugeFaim, JaugeFatigue, JaugeReproduction, pos=None):
        print("CarnivoreBody created")
        print("At pos : " + str(pos))
        super().__init__(JaugeFaim, JaugeFatigue, JaugeReproduction, pos)
        self.color = (255, 0, 0)
        self.velocity = Vector2(0, 0)
        self.bodySize = 10

    def show(self):
        if not self.isDead:
            core.Draw.circle(self.color, self.position, self.bodySize)
        else:
            pass
            core.Draw.circle((211,211,211), self.position, self.bodySize)

    def reproduction(self):
        from CarnivoreAgent import CarnivoreAgent
        c = CarnivoreAgent(CarnivoreBody(PersonalRandom.randomJaugeFaim(PersonalRandom()),
                                         PersonalRandom.randomJaugeFatigue(PersonalRandom()),
                                         PersonalRandom.randomJaugeReproduction(PersonalRandom()),
                                         self.position+Vector2(random.randint(-1, 1), random.randint(-1, 1))))
        core.memory('agents').append(c)

