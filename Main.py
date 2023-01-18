import random
import time
import json

from pygame import Vector2

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
    loadJsonScenario()
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [600, 700]

    core.memory("agents", [])
    core.memory("items", [])
    core.memory("timer", time.time())
    print(core.memory("scenario")['SuperPredateur']['nb'])

    for i in range(0, core.memory("scenario")['SuperPredateur']['nb']):
        core.memory('agents').append(SuperPredateurAgent(SuperPredateurBody()))
    for i in range(0, core.memory("scenario")['Carnivore']['nb']):
        core.memory('agents').append(CarnivoreAgent(CarnivoreBody()))
    for i in range(0,core.memory("scenario")['Decomposeur']['nb']):
        core.memory('agents').append(HerbivoreAgent(HerbivoreBody()))
    for i in range(0, core.memory("scenario")['Herbivore']['nb']):
        core.memory('agents').append(DecomposeurAgent(DecomposeurBody()))
    for i in range(0, core.memory("scenario")['Vegetal']['nb']):
        core.memory('items').append(VegetalItem())

    print("Setup END-----------")

def loadJsonScenario():
    # Open the file
    a = "scenario.json"
    with open(a) as json_file:
        # Load the JSON data from the file
        data = json.load(json_file)
    core.memory("scenario", data)

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
    #a.body.bordure(core.WINDOW_SIZE)


def updateEnv():
    for a in core.memory("agents"):
        if a.body.isDead:
            break
        if isinstance(a, DecomposeurAgent):
            if a.body.isDead:
                core.memory("agents").remove(a)
                continue
        for b in core.memory("agents"):
            if a.uuid != b.uuid:
                if (a.body.position.distance_to(b.body.position)) <= a.body.bodySize + b.body.bodySize:
                    if a.doMange(b):
                        if isinstance(a, DecomposeurAgent):
                            if b.body.isDead:
                                core.memory("agents").remove(b)
                                core.memory("items").append(VegetalItem(a.body.position+Vector2(random.randint(-1, 1), random.randint(-1, 1))))
                        else:
                            b.body.isDead = True
                            if hasattr(a, "jaugeFaim"):
                                a.body.jaugeFaim.value = a.body.jaugeFaim.min
        for c in core.memory("items"):
            if (a.body.position.distance_to(c.position)) <= a.body.bodySize + c.bodySize:
                if a.doMange(c):
                    core.memory("items").remove(c)
                    if hasattr(a, "jaugeFaim"):
                        a.body.jaugeFaim.value = a.body.jaugeFaim.min


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


    updateEnv()


core.main(setup, run)
