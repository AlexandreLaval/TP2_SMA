import random
import time

from CarnivoreAgent import CarnivoreAgent
from DecomposeurAgent import DecomposeurAgent
from HerbivoreAgent import HerbivoreAgent
from SuperPredateurAgent import SuperPredateurAgent
from CarnivoreBody import CarnivoreBody
from DecomposeurBody import DecomposeurBody
from HerbivoreBody import HerbivoreBody
from SuperPredateurBody import SuperPredateurBody

import core
from VegetalItem import VegetalItem
from Jauge import Jauge


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [600, 600]

    core.memory("superpredateurs", [])
    core.memory("carnivores", [])
    core.memory("herbivores", [])
    core.memory("decomposeurs", [])
    core.memory("vegetaux", [])
    core.memory("agents", [])
    core.memory("items", [])
    core.memory("timer", time.time())

    for i in range(0, 1):
        Sp = SuperPredateurAgent(SuperPredateurBody(randomJaugeFaim(), randomJaugeFatigue(), randomJaugeReproduction()))
        core.memory('agents').append(Sp)
        core.memory('carnivores').append(Sp)
    for i in range(0, 1):
        core.memory('agents').append(CarnivoreAgent(CarnivoreBody(randomJaugeFaim(),randomJaugeFatigue(), randomJaugeReproduction())))
    for i in range(0, 1):
        core.memory('agents').append(HerbivoreAgent(HerbivoreBody(randomJaugeFaim(),randomJaugeFatigue(), randomJaugeReproduction())))
    for i in range(0, 1):
        core.memory('agents').append(DecomposeurAgent(DecomposeurBody(randomJaugeFaim(),randomJaugeFatigue(), randomJaugeReproduction())))
    for i in range(0,1):
        core.memory('items').append(VegetalItem())

    print("Setup END-----------")

def randomJaugeFaim():
    return Jauge(random.randint(0,1), random.randint(15,25), 2)
def randomJaugeReproduction():
    return Jauge(random.randint(0,5), random.randint(5,10), 2)
def randomJaugeFatigue():
    return Jauge(random.randint(0,5), random.randint(20,30), 1)
def computePerception(a):
    a.body.fustrum.perceptionList = []
    for b in core.memory('agents'):
        if a.uuid != b.uuid:
            if a.body.fustrum.inside(b.body):
                a.body.fustrum.perceptionList.append(b.body)
    for b in core.memory('items'):
        if a.body.fustrum.inside(b):
            a.body.fustrum.perceptionList.append(b)


def computeDecision(a):
    a.update()


def applyDecision(a):
    a.body.update()


def run():
    core.cleanScreen()

    # Display
    for item in core.memory("items"):
        item.show()

    for agent in core.memory("agents"):
        agent.show()

    for agent in core.memory("agents"):
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)

core.main(setup, run)
