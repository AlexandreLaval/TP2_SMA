from Agent import Agent
from CarnivoreBody import CarnivoreBody


class SuperPredateurAgent(Agent):
    def __init__(self, body):
        super().__init__(body)

    def doMange(self, proie):
        if type(proie).__name__ == CarnivoreBody.__class__.__name__:
            return True
    def update(self):
        if not self.body.isDead:
            preys, predateurs = self.filterPerception()
            self.computeForce(preys, predateurs)
    def filterPerception(self):
        proies = []
        predateurs = []
        for i in self.body.fustrum.perceptionList:
            if type(i).__name__ == CarnivoreBody.__class__.__name__:
                if not i.isDead:
                    proies.append(i)
        return proies, predateurs
