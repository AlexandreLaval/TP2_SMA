from Agent import Agent


class DecomposeurAgent(Agent):
    def __init__(self, body):
        super().__init__(body)

    def doMange(self, proie):
        if hasattr(proie, 'isDead'):
            if proie.isDead:
                return True

    def update(self):
        if not self.body.isDead:
            preys, predateurs = self.filterPerception()
            self.computeForce(preys, predateurs)

    def filterPerception(self):
        proies = []
        predateurs = []
        for i in self.body.fustrum.perceptionList:
            if hasattr(i, 'isDead'):
                if i.isDead:
                    proies.append(i)
        return proies, predateurs
