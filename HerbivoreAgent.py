from Agent import Agent
from CarnivoreBody import CarnivoreBody
from VegetalItem import VegetalItem


class HerbivoreAgent(Agent):
    def __init__(self, body):
        super().__init__(body)

    def update(self):
        if not self.body.isDead:
            preys, predateurs = self.filterPerception()
            self.computeForce(preys, predateurs)
    def filterPerception(self):
        proies = []
        predateurs = []
        for i in self.body.fustrum.perceptionList:
            if type(i).__name__ == VegetalItem.__class__.__name__:
                proies.append(i)
            if type(i).__name__ == CarnivoreBody.__class__.__name__:
                if not i.isDead:
                    predateurs.append(i)
        return proies, predateurs
