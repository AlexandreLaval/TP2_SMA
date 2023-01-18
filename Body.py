import random
import time

from pygame import Vector2

import core
from Fustrum import Fustrum
from Jauge import Jauge


class Body(object):
    def __init__(self, pos=None):
        if (pos is None):
            self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        else:
            self.position = pos
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.fustrum = Fustrum(100, self)
        self.velocity = Vector2()
        self.acceleration = Vector2()
        self.bodySize = 8
        self.birthTime = time.time()
        self.esperance = 1000  # en seconde
        self.isDead = False
        self.isSleeping = False
        self.isStarving = False

    def update(self):
        if not self.isDead:
            if not self.isSleeping:
                if self.acceleration.length() > self.maxAcc:
                    self.acceleration.scale_to_length(self.maxAcc)

                self.velocity += self.acceleration
                if self.velocity.length() > self.maxSpeed:
                    self.velocity.scale_to_length(self.maxSpeed)

                self.acceleration = Vector2(0, 0)
                self.position += self.velocity
                self.checkAll()
                self.jaugeReproduction.evolution()
                self.jaugeFaim.evolution()
                self.jaugeFatigue.evolution()
        else:
            self.velocity = Vector2()
            self.acceleration = Vector2()

    def checkAll(self):
        self.checkEsperance()
        self.checkReproduction()
        self.checkJaugeFatigue()
        self.checkJaugeFaim()

    def checkEsperance(self):
        if self.esperance < time.time() - self.birthTime:
            self.isDead = True

    def checkReproduction(self):
        if (self.jaugeReproduction.value > self.jaugeReproduction.max):
            self.jaugeReproduction.value = self.jaugeReproduction.max
            self.jaugeReproduction.increase = not self.jaugeReproduction.increase
            self.reproduction()

    def reproduction(self):
        pass

    def checkJaugeFatigue(self):
        if self.jaugeFatigue.value >= self.jaugeFatigue.max:
            self.jaugeFatigue.value = self.jaugeFatigue.max
            self.isSleeping = True
        elif self.jaugeFatigue.value <= self.jaugeFatigue.min:
            self.jaugeFatigue.value = self.jaugeFatigue.min
            self.isSleeping = False

    def checkJaugeFaim(self):
        if self.jaugeFaim.value >= self.jaugeFaim.max:
            print("je suis mort de faim")
            self.jaugeFaim.value = self.jaugeFaim.max
            self.isDead = True

    def evolutionJauges(self):
        self.jaugeFaim.evolution()
        self.jaugeFatigue.evolution()
        self.jaugeReproduction.evolution()

    def show(self):
        if self.isSleeping:
            pass
        if self.isStarving:
            pass

    def edge(self):
        if self.position.x <= self.bodySize:
            self.velocity.x *= -1
        if self.position.x + self.bodySize >= core.WINDOW_SIZE[0]:
            self.velocity.x *= -1
        if self.position.y <= self.bodySize:
            self.velocity.y *= -1
        if self.position.y + self.bodySize >= core.WINDOW_SIZE[1]:
            self.velocity.y *= -1

    # def bordure(self, fenetre):
    #     if self.position.y < 0:
    #         self.position.y = fenetre[1]
    #
    #     if self.position.y > fenetre[1]:
    #         self.position.y = 0
    #
    #     if self.position.x < 0:
    #         self.position.x = fenetre[0]
    #
    #     if self.position.x > fenetre[0]:
    #         self.position.x = 0
