import random

from pygame import Vector2


class Agent(object):
    def __init__(self, body):
        self.body = body
        self.uuid = random.randint(100000, 999999999)

    def update(self):
        pass

    def show(self):
        self.body.show()
