from scripts import ArtilleryBattery
from scripts import ForwardObserver
from utils import Coordinate
from ursina import Entity, Text

class Game(Entity):
    """
    Main game class to manage the artillery game scenario.
    """
    def __init__(self,result_text: Text):
        super().__init__()
        self.battery = ArtilleryBattery()
        self.observer = ForwardObserver(Coordinate(100, 100))
        self.target = Coordinate(200, 200)
        self.result_text = result_text

    def run_mission(self):
        """Simulates a single fire mission in the game."""
        result = self.observer.call_for_fire(self.target, self.battery)
        if result:
            self.result_text.text = "Target hit successfully!"
        else:
            self.result_text.text = "Mission failed or target missed."

    def play(self, rounds=1):
        """
        Plays the game for a specified number of rounds.

        :param rounds: Number of fire missions to simulate.
        """
        for _ in range(rounds):
            self.run_mission()