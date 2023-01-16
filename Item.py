import random

from pygame import Vector2

import core

class Item(object):
    def __init__(self, pos = None):
        self.color = (255, 255, 255)
        if pos is None:
            self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        else:
            self.position = pos
        self.bodySize = 5

    def show(self):
        core.Draw.rect(self.color, (self.position, (5, 5)), self.bodySize)
