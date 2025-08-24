import random
from car import Car


class UnreliableCar(Car):
    """A Car that may fail to drive depending on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar with name, fuel, and reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if a random chance is within its reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
