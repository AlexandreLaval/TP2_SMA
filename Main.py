import time

from Agents.CarnivoreAgent import CarnivoreAgent
from Agents.DecomposeurAgent import DecomposeurAgent
from Agents.HerbivoreAgent import HerbivoreAgent
from Agents.SuperPredateurAgent import SuperPredateurAgent
from Agents.VegetalAgent import VegetalAgent
from Bodies.VegetalBody import VegetalBody
from Bodies.CarnivoreBody import CarnivoreBody
from Bodies.DecomposeurBody import DecomposeurBody
from Bodies.HerbivoreBody import HerbivoreBody
from Bodies.SuperPredateurBody import SuperPredateurBody
from Item import Item

import core
from Agents.Agent import Agent
from Bodies.Body import Body


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
        core.memory('agents').append(SuperPredateurAgent(SuperPredateurBody()))
    for i in range(0, 1):
        core.memory('agents').append(CarnivoreAgent(CarnivoreBody()))
    for i in range(0, 1):
        core.memory('agents').append(HerbivoreAgent(HerbivoreBody()))
    for i in range(0, 1):
        core.memory('agents').append(DecomposeurAgent(DecomposeurBody()))
    for i in range(0,1):
        core.memory('agents').append(VegetalAgent(VegetalBody()))

    print("Setup END-----------")


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
