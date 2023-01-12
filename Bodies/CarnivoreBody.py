import core
from Bodies.Body import Body


class CarnivoreBody(Body):
    def __init__(self):
        super().__init__()
        self.color = (255, 0, 0)
        self.bodySize = 10

    def show(self):
        core.Draw.circle(self.color, self.position, self.bodySize)