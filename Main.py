import json
import random
import threading
import time

import matplotlib.pyplot as plt
import pygame.time
from pygame import Vector2

import core
from Agents.CarnivoreAgent import CarnivoreAgent
from Agents.DecomposeurAgent import DecomposeurAgent
from Agents.HerbivoreAgent import HerbivoreAgent
from Agents.SuperPredateurAgent import SuperPredateurAgent
from Bodies.CarnivoreBody import CarnivoreBody
from Bodies.DecomposeurBody import DecomposeurBody
from Bodies.HerbivoreBody import HerbivoreBody
from Bodies.SuperPredateurBody import SuperPredateurBody
from Items.VegetalItem import VegetalItem


def setup():
    loadJsonScenario()
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]

    core.memory("agents", [])
    core.memory("items", [])
    core.memory("timer", time.time())
    print(core.memory("scenario")['SuperPredateur']['nb'])

    for i in range(0, core.memory("scenario")['SuperPredateur']['nb']):
        core.memory('agents').append(SuperPredateurAgent(SuperPredateurBody()))
    for i in range(0, core.memory("scenario")['Carnivore']['nb']):
        core.memory('agents').append(CarnivoreAgent(CarnivoreBody()))
    for i in range(0, core.memory("scenario")['Herbivore']['nb']):
        core.memory('agents').append(HerbivoreAgent(HerbivoreBody()))
    for i in range(0, core.memory("scenario")['Decomposeur']['nb']):
        core.memory('agents').append(DecomposeurAgent(DecomposeurBody()))
    for i in range(0, core.memory("scenario")['Vegetal']['nb']):
        core.memory('items').append(VegetalItem())

    plotThread = threading.Thread(target=drawEvolution, args=())
    plotThread.start()
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
    a.body.bordure(core.WINDOW_SIZE)


def updateEnv():
    for a in core.memory("agents"):
        if isinstance(a, DecomposeurAgent):
            if a.body.isDead:
                core.memory("agents").remove(a)
        if not a.body.isDead:
            for b in core.memory("agents"):
                if a.uuid != b.uuid:
                    if (a.body.position.distance_to(b.body.position)) <= a.body.bodySize + b.body.bodySize:
                        if a.doMange(b):
                            if isinstance(a, DecomposeurAgent):
                                if b.body.isDead:
                                    core.memory("agents").remove(b)
                                    core.memory("items").append(VegetalItem(
                                        a.body.position + Vector2(random.randint(-1, 1), random.randint(-1, 1))))
                            else:
                                if not b.body.isDead:
                                    b.body.isDead = True
                                    if hasattr(a, "jaugeFaim"):
                                        a.body.jaugeFaim.value = a.body.jaugeFaim.min
            for c in core.memory("items"):
                if (a.body.position.distance_to(c.position)) <= a.body.bodySize + c.bodySize:
                    if a.doMange(c):
                        core.memory("items").remove(c)
                        if hasattr(a, "jaugeFaim"):
                            a.body.jaugeFaim.value = a.body.jaugeFaim.min


def getBestIndividual():
    bestGenStats = 0
    bestAgent = None
    for a in core.memory('agents'):
        if a.body.quantumGenetetic() > bestGenStats:
            bestGenStats = a.body.quantumGenetetic()
            bestAgent = a
    return bestAgent

def showBestIndividual():
    agent = getBestIndividual()
    print("Le meilleur individu est -----------")
    print("un agent de type : " + str(agent.__class__.__name__ ))
    print("avec un core génétique de : " + str(int(agent.body.quantumGenetetic())))
    print("-----------")

def showAgentsRepartition():
    herbivores = []
    carnivores = []
    superPredators = []
    decomposeurs = []
    for a in core.memory('agents'):
        if not a.body.isDead:
            if isinstance(a, HerbivoreAgent):
                herbivores.append(a)
            elif isinstance(a, CarnivoreAgent):
                carnivores.append(a)
            elif isinstance(a, SuperPredateurAgent):
                superPredators.append(a)
            elif isinstance(a, DecomposeurAgent):
                decomposeurs.append(a)
    print("Stats BEGIN -----------")
    print("herbivores: " + str(int(len(herbivores) / len(core.memory('agents')) * 100)) + "%")
    print("carnivores: " + str(int(len(carnivores) / len(core.memory('agents')) * 100)) + "%")
    print("superPredators: " + str(int(len(superPredators) / len(core.memory('agents')) * 100)) + "%")
    print("decomposeurs: " + str(int(len(decomposeurs) / len(core.memory('agents')) * 100)) + "%")
    print("Stats END-----------")


history_time = []
history_data = {"Herbivores": [], "Vegetaux": [], "Carnivores": [], "SuperPredateurs": [], "Decomposeurs": [],
                'Morts': []}


def drawEvolution():
    while True:
        global history_data
        global history_time

        data = {'Herbivores': 0, 'Vegetaux': 0, 'Carnivores': 0, 'SuperPredateurs': 0, 'Decomposeurs': 0, 'Morts': 0}

        for a in core.memory("agents"):
            if a.body.isDead:
                data["Morts"] += 1
            elif isinstance(a, HerbivoreAgent):
                data["Herbivores"] += 1
            elif isinstance(a, CarnivoreAgent):
                data["Carnivores"] += 1
            elif isinstance(a, SuperPredateurAgent):
                data["SuperPredateurs"] += 1
            elif isinstance(a, DecomposeurAgent):
                data["Decomposeurs"] += 1

        for i in core.memory("items"):
            data["Vegetaux"] += 1

        plt.cla()
        current_time = pygame.time.get_ticks() / 1000
        history_time.append(current_time)
        for key in history_data.keys():
            history_data[key].append(data[key])
            if key == "Morts":
                plt.plot(history_time, history_data[key], 'grey', label=key)
            elif key == "Herbivores":
                plt.plot(history_time, history_data[key], 'green', label=key)
            elif key == "Carnivores":
                plt.plot(history_time, history_data[key], 'red', label=key)
            elif key == "SuperPredateurs":
                plt.plot(history_time, history_data[key], 'blue', label=key)
            elif key == "Decomposeurs":
                plt.plot(history_time, history_data[key], 'brown', label=key)
            elif key == "Vegetaux":
                plt.plot(history_time, history_data[key], 'olive', label=key)

        plt.xlabel("Temps en secondes")
        plt.ylabel("Nombre d\'individu")
        plt.title("Evolution du nombre d\'individu en fonction du temps")
        plt.legend(loc="center left")
        plt.ion()
        plt.draw()
        plt.show()
        plt.pause(0.001)


def run():
    core.cleanScreen()

    if core.getMouseLeftClick():
        showAgentsRepartition()

    if core.getMouseRightClick():
        showBestIndividual()

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
