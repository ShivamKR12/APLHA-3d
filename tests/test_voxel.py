import unittest
from ursina import Ursina, Entity, color, mouse
from main import Voxel

class TestVoxel(unittest.TestCase):

    def setUp(self):
        self.app = Ursina()
        self.voxel = Voxel(position=(0,0,0))

    def test_block_placement(self):
        initial_position = self.voxel.position
        self.voxel.input('left mouse down')
        new_voxel = Voxel(position=initial_position + mouse.normal)
        self.assertEqual(new_voxel.position, initial_position + mouse.normal)

    def test_block_removal(self):
        self.voxel.input('right mouse down')
        self.assertIsNone(self.voxel)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.voxel.input('invalid key')

    def test_chunk_handling(self):
        chunk = [Voxel(position=(x,0,z)) for x in range(8) for z in range(8)]
        self.assertEqual(len(chunk), 64)
        for voxel in chunk:
            self.assertIsInstance(voxel, Voxel)

if __name__ == '__main__':
    unittest.main()
