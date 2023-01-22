from Items.Item import Item


class VegetalItem(Item):
    def __init__(self, pos = None):
        super().__init__(pos)
        self.color = (0, 255, 0)

    def show(self):
        super().show()
