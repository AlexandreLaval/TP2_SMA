import core
from Bodies.Body import Body


class HerbivoreBody(Body):
    def __init__(self):
        super().__init__()
        self.color = (88, 41, 0)

    def show(self):
        core.Draw.circle(self.color, self.position, self.bodySize)
