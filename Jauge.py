import time


class Jauge(object):
    def __init__(self, max, fulfillmentSpeed):
        self.min = 0
        self.max = max
        self.value = 0
        self.time = time.time()
        self.fulfillmentSpeed = fulfillmentSpeed
        self.increase = True

    def evolution(self):
        if self.increase:
            if self.value < self.max:
                self.value += self.fulfillmentSpeed * (time.time() - self.time)
                self.time = time.time()
        else:
            if self.value > self.min:
                self.value -= self.fulfillmentSpeed * (time.time() - self.time)
                self.time = time.time()