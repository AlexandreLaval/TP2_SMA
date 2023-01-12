import time


class Jauge(object):
    def __init__(self, min, max, fulfillmentSpeed):
        self.min = min
        self.max = max
        self.value = min
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