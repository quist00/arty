from ursina import Ursina, Entity, color, Vec3, time, held_keys, Text
from scripts import ArtilleryBattery, ForwardObserver
from scripts.game import Game
from utils import Coordinate

app = Ursina()

# Example player entity
player = Entity(model='cube', color=color.blue, scale=(1, 2, 1), position=Vec3(0, 1, 0))
enemy = Entity(model='sphere', color=color.red, scale=(1, 2, 1), position=Vec3(2, 1, 0))  

# Text entity to display results
result_text = Text(text='', position=(-0.5, 0.4), origin=(0, 0), scale=2)

game = Game(result_text)

# Example update function
def update():
    pass
    player.x += held_keys['d'] * time.dt
    player.x -= held_keys['a'] * time.dt
    player.y += held_keys['w'] * time.dt
    player.y -= held_keys['s'] * time.dt

    # Example of running the game logic
    if held_keys['space']:
        game.play(rounds=5)

app.run()