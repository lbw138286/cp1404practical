from car import Car
import random

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        chance = random.uniform(0, 100)
        if chance < self.reliability:
            return super().drive(distance)
        return 0