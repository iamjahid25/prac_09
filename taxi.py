from car import Car


class Taxi(Car):
    """A Car that includes fare calculation based on distance."""

    price_per_km = 1.23  # class variable as per instruction

    def __init__(self, name, fuel):
        """Initialize a Taxi with name, fuel, and reset fare distance."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return Taxi details including fare distance and rate per km."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        """Return the total fare for the current trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Reset the fare distance for a new trip."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive the car and update the current fare distance."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
