import random

from pygame import Vector2


class Agent(object):
    def __init__(self, body):
        self.body = body
        self.uuid = random.randint(100000, 999999999)

    def update(self):
        pass



    # def wantToEat(self):
    #     if self.body.jaugeFaim.value > self.body.jaugeFaim.max / 2:
    #         return True
    #
    # def fear(self, predators):
    #     steering = Vector2()
    #     predatorCounter = 0
    #     for other in predators:
    #         if self.body.position.distance_to(other.position) != 0:
    #             diff = Vector2(other.position.x - self.body.position.x, other.position.y - self.body.position.y)
    #             if diff.length() > 0.001:
    #                 diff.scale_to_length(self.body.position.distance_squared_to(other.position))
    #                 predatorCounter += 1
    #                 steering += diff
    #         else:
    #             steering += Vector2(random.uniform(-5, 5), random.uniform(-5, 5))
    #             predatorCounter += 1
    #
    #     if predatorCounter > 0:
    #         steering /= predatorCounter
    #
    #         steering += self.body.velocity
    #
    #         if steering.length() > self.body.maxAcc:
    #             steering = steering.normalize()
    #             steering.scale_to_length(self.body.maxAcc)
    #     return steering

    def show(self):
        self.body.show()
