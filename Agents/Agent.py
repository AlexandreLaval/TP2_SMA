import random

from pygame import Vector2


class Agent(object):
    def __init__(self, body):
        self.body = body
        self.uuid = random.randint(100000, 999999999)

    def update(self):
        # Random movement
        target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
        while target.length() == 0:
            target = Vector2(random.randint(-1, 1), random.randint(-1, 1))

        target.scale_to_length(target.length() * 0.01)
        self.body.acceleration += target

    def filterPerception(self):
        everybody = []
        masks = []
        for i in self.body.fustrum.perceptionList:
            if hasattr(i, 'position'):
                    everybody.append(i)
            else:
                masks.append(i)
        return everybody, masks



    def show(self):
        self.body.show()
