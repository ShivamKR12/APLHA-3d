import unittest
from ursina import Ursina, Entity, Vec3, color, mouse
from ursina.prefabs.first_person_controller import FirstPersonController

class Voxel(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            model='cube',
            color=color.white,
            texture='white_cube',
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
                return True
        return False

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

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.app = Ursina()
        self.player = FirstPersonController()
        self.inventory = Inventory()
        self.crafting_system = CraftingSystem(self.inventory)
        self.voxel = Voxel(position=(0,0,0))

    def test_player_actions(self):
        initial_voxel_count = len(self.app.entities)
        self.voxel.input('left mouse down')
        self.assertEqual(len(self.app.entities), initial_voxel_count + 1)
        self.voxel.input('right mouse down')
        self.assertEqual(len(self.app.entities), initial_voxel_count)

    def test_crafting_system(self):
        self.inventory.add_item('wood', 2)
        self.inventory.add_item('stone', 3)
        self.assertTrue(self.crafting_system.craft('stone_pickaxe'))
        self.assertFalse(self.crafting_system.craft('stone_shovel'))

    def test_entity_behavior(self):
        npc = Entity(model='cube', color=color.random_color(), position=(0,0,0), scale=0.5)
        initial_position = npc.position
        npc.position += Vec3(1, 0, 0)
        self.assertNotEqual(initial_position, npc.position)

    def test_game_state_transitions(self):
        initial_position = self.player.position
        self.player.position += Vec3(1, 0, 0)
        self.assertNotEqual(initial_position, self.player.position)
        self.player.position = initial_position
        self.assertEqual(initial_position, self.player.position)

    def test_game_mechanics(self):
        self.inventory.add_item('wood', 2)
        self.inventory.add_item('stone', 3)
        self.assertTrue(self.crafting_system.craft('stone_pickaxe'))
        self.assertFalse(self.crafting_system.craft('stone_shovel'))
        self.voxel.input('left mouse down')
        self.assertEqual(self.voxel.color, color.white)

if __name__ == '__main__':
    unittest.main()
