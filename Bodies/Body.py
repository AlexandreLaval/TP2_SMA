import random
import time

from pygame import Vector2

import core
from Fustrum import Fustrum
from Jauge import Jauge


class Body(object):
    def __init__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.fustrum = Fustrum(100, self)
        self.velocity = Vector2()
        self.acceleration = Vector2()
        self.maxAcc = 1
        self.maxSpeed = 4
        self.bodySize = 8
        self.jaugeFaim = Jauge(0,10,0)
        self.jaugeFatigue = Jauge(0,10,0)
        self.jaugeReproduction = Jauge(0,10,0)
        self.birthTime = time.time()
        self.esperance = 100 #en seconde


    def update(self):
        if self.acceleration.length() > self.maxAcc:
            self.acceleration.scale_to_length(self.maxAcc)

        self.velocity += self.acceleration
        if self.velocity.length() > self.maxSpeed:
            self.velocity.scale_to_length(self.maxSpeed)

        self.acceleration = Vector2(0, 0)
        self.position += self.velocity
        self.edge()

    def show(self):
        core.Draw.circle(self.color, self.position, self.bodySize)

    def edge(self):
        if self.position.x <= self.bodySize:
            self.velocity.x *= -1
        if self.position.x + self.bodySize >= core.WINDOW_SIZE[0]:
            self.velocity.x *= -1
        if self.position.y <= self.bodySize:
            self.velocity.y *= -1
        if self.position.y + self.bodySize >= core.WINDOW_SIZE[1]:
            self.velocity.y *= -1
