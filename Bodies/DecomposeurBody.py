import core
from Bodies.Body import Body


class DecomposeurBody(Body):
    def __init__(self):
        super().__init__()
        self.color = (0, 255, 0)


    def show(self):
        core.Draw.circle(self.color, self.position, self.bodySize)