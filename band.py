class Band:
    """A band with a name and a list of musicians."""

    def __init__(self, name):
        """Initialize a Band with a name and an empty musician list."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return the band name and musician names as a string."""
        return f"{self.name} ({', '.join(musician.name for musician in self.musicians)})"

    def play(self):
        """Return a string of all musicians playing their instruments."""
        return "\n".join(musician.play() for musician in self.musicians)
