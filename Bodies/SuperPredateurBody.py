from Bodies.Body import Body


class SuperPredateurBody(Body):
    def __init__(self):
        super().__init__()
        self.color = (0, 0, 255)
