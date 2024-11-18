from ursina import Ursina, Entity, Button, mouse, held_keys, Vec3, color
from ursina.prefabs.first_person_controller import FirstPersonController

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] -= quantity
            if self.items[item] <= 0:
                del self.items[item]

    def has_item(self, item, quantity=1):
        return self.items.get(item, 0) >= quantity

class Tool(Entity):
    def __init__(self, name, break_speed):
        super().__init__()
        self.name = name
        self.break_speed = break_speed

class Voxel(Entity):
    def __init__(self, position=(0,0,0), texture='white_cube'):
        super().__init__(
            model='cube',
            color=color.white,
            texture=texture,
            position=position
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position=self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)

class CraftingSystem:
    def __init__(self, inventory):
        self.inventory = inventory
        self.recipes = {
            'stone_pickaxe': {'wood': 2, 'stone': 3},
            'stone_shovel': {'wood': 1, 'stone': 2}
        }

    def craft(self, item):
        if item in self.recipes:
            recipe = self.recipes[item]
            if all(self.inventory.has_item(ingredient, quantity) for ingredient, quantity in recipe.items()):
                for ingredient, quantity in recipe.items():
                    self.inventory.remove_item(ingredient, quantity)
                self.inventory.add_item(item)
                print(f"Crafted {item}")
            else:
                print("Not enough resources to craft", item)
        else:
            print("Unknown recipe:", item)

app = Ursina()

inventory = Inventory()
crafting_system = CraftingSystem(inventory)

for z in range(8):
    for x in range(8):
        Voxel(position=(x,0,z))

player = FirstPersonController()

app.run()
