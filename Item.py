import random

from pygame import Vector2

import core

class Item(object):
    def __init__(self):
        self.color = (255,255,255)
        self.position=Vector2(random.randint(0,core.WINDOW_SIZE[0]),random.randint(0,core.WINDOW_SIZE[1]))

    def show(self):
        core.Draw.rect(self.color, (self.position, (15,5)), 3)