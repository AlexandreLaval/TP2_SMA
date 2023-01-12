import random

from Jauge import Jauge


class PersonalRandom(object):
    def __init__(self):
        self.randomJaugeFaim = Jauge(random.randint(0, 1), random.randint(20, 35), 2)
        self.randomJaugeReproduction = Jauge(random.randint(0, 5), random.randint(5, 10), 2)
        self.randomJaugeFatigue = Jauge(random.randint(0, 5), random.randint(20, 30), 1)

    def randomJaugeFaim(self):
        return Jauge(random.randint(0, 1), random.randint(20, 35), 2)

    def randomJaugeReproduction(self):
        return Jauge(random.randint(0, 5), random.randint(5, 10), 2)

    def randomJaugeFatigue(self):
        return Jauge(random.randint(0, 5), random.randint(20, 30), 1)