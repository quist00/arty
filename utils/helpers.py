import math

class Coordinate:
    """
    Represents a coordinate on a 2D plane, typically used for target or observer positions.
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        """Calculate the Euclidean distance between two coordinates."""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)