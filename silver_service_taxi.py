from taxi import Taxi

FLAGFALL = 4.50


class SilverServiceTaxi(Taxi):
    """A Taxi with fanciness multiplier and a fixed flagfall charge."""

    def __init__(self, name: str, fuel: float, fanciness: float):
        """Initialize a SilverServiceTaxi with name, fuel, and fanciness."""
        super().__init__(name, fuel)
        self.fanciness: float = max(1.0, fanciness)  # Prevent fanciness < 1
        self.price_per_km *= self.fanciness

    def get_fare(self) -> float:
        """Return the fare including the flagfall."""
        return round(super().get_fare() + FLAGFALL, 2)

    def __str__(self) -> str:
        """Return the taxi details including fanciness and flagfall."""
        return f"{super().__str__()}, fanciness x{self.fanciness:.1f}, plus flagfall of ${FLAGFALL:.2f}"
