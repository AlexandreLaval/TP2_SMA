from Item import Item


class VegetalItem(Item):
    def __init__(self):
        super().__init__()
        self.color = (255, 255, 255)

    def show(self):
        super().show()
