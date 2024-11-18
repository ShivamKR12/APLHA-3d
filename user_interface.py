from ursina import Ursina, Entity, Text, Button, camera, Vec3
from ursina.prefabs.first_person_controller import FirstPersonController

class HUD(Entity):
    def __init__(self):
        super().__init__()
        self.inventory_text = Text(text='Inventory: ', position=(-0.5, 0.4), scale=2)
        self.coordinates_text = Text(text='Coordinates: ', position=(-0.5, 0.35), scale=2)
        self.health_text = Text(text='Health: ', position=(-0.5, 0.3), scale=2)

    def update(self, inventory, coordinates, health):
        self.inventory_text.text = f'Inventory: {inventory}'
        self.coordinates_text.text = f'Coordinates: {coordinates}'
        self.health_text.text = f'Health: {health}'

class Menu(Entity):
    def __init__(self):
        super().__init__()
        self.settings_button = Button(text='Settings', position=(-0.5, 0.2), scale=0.1)
        self.world_creation_button = Button(text='World Creation', position=(-0.5, 0.1), scale=0.1)
        self.save_button = Button(text='Save', position=(-0.5, 0.0), scale=0.1)
        self.load_button = Button(text='Load', position=(-0.5, -0.1), scale=0.1)

class Minimap(Entity):
    def __init__(self):
        super().__init__()
        self.minimap = Entity(model='quad', color=color.gray, scale=(0.2, 0.2), position=(0.7, 0.4))
        self.player_marker = Entity(model='quad', color=color.red, scale=(0.02, 0.02), parent=self.minimap)

    def update(self, player_position):
        self.player_marker.position = Vec3(player_position.x / 100, player_position.z / 100, 0)

app = Ursina()

hud = HUD()
menu = Menu()
minimap = Minimap()

player = FirstPersonController()

def update():
    hud.update(inventory='Wood: 10, Stone: 5', coordinates=player.position, health=100)
    minimap.update(player.position)

app.run()
