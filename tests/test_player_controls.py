import unittest
from ursina import Ursina, Entity, Vec3, color
from ursina.prefabs.first_person_controller import FirstPersonController

class TestPlayerControls(unittest.TestCase):

    def setUp(self):
        self.app = Ursina()
        self.player = FirstPersonController()
        self.voxel = Voxel(position=(0,0,0))

    def test_player_movement(self):
        initial_position = self.player.position
        self.player.position += Vec3(1, 0, 0)
        self.assertNotEqual(initial_position, self.player.position)

    def test_player_collision(self):
        self.player.position = Vec3(0, 1, 0)
        self.player.update()
        self.assertEqual(self.player.position.y, 1)

    def test_block_placement(self):
        initial_voxel_count = len(self.app.entities)
        self.voxel.input('left mouse down')
        self.assertEqual(len(self.app.entities), initial_voxel_count + 1)

    def test_block_removal(self):
        initial_voxel_count = len(self.app.entities)
        self.voxel.input('right mouse down')
        self.assertEqual(len(self.app.entities), initial_voxel_count - 1)

if __name__ == '__main__':
    unittest.main()
