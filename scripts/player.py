import random
from utils import Coordinate

class ArtilleryBattery:
    """
    Represents an artillery battery capable of firing missions.
    """
    def __init__(self, location=Coordinate(0, 0)):
        self.location = location
        self.guns = 6  # Default number of guns in a battery

    def fire_mission(self, target, shell_type="HE", fuse="QT"):
        """
        Simulates firing a mission.

        :param target: Coordinate object representing the target location.
        :param shell_type: Type of shell to use (default is High Explosive).
        :param fuse: Fuse setting (default is Quick Time).
        :return: Boolean indicating if the mission was successful.
        """
        # Simple simulation of firing accuracy
        accuracy = random.uniform(0, 1)
        return accuracy > 0.3  # 70% chance of success for simplicity

class ForwardObserver:
    """
    Represents a forward observer who calls for fire missions.
    """
    def __init__(self, location=Coordinate(0, 0)):
        self.location = location

    def call_for_fire(self, target, battery):
        """
        Calls for a fire mission from the given battery to the target.

        :param target: Coordinate of the target.
        :param battery: ArtilleryBattery object to execute the mission.
        :return: Result of the fire mission.
        """
        if self.location.distance(target) < 10:  # Simple safety check
            print("Too close to target, aborting mission.")
            return False
        return battery.fire_mission(target)