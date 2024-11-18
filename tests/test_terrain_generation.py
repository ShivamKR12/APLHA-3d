import unittest
from terrain_features import Terrain, Water, Cave, Biome, TerrainVariation
from ursina import color

class TestTerrainGeneration(unittest.TestCase):

    def setUp(self):
        self.terrain = Terrain()

    def test_biomes(self):
        for z in range(20):
            for x in range(20):
                biome = Biome(position=(x, 0, z), biome_type='forest' if (x + z) % 3 == 0 else 'desert' if (x + z) % 3 == 1 else 'mountains')
                self.assertIn(biome.color, [color.green, color.yellow, color.gray])

    def test_terrain_variations(self):
        for z in range(5, 15):
            for x in range(5, 15):
                variation = TerrainVariation(position=(x, 3, z), variation_type='cave' if (x + z) % 2 == 0 else 'overhang')
                self.assertIn(variation.color, [color.black, color.brown])

    def test_water_block_physics(self):
        for z in range(20):
            for x in range(20):
                water = Water(position=(x, -1, z))
                self.assertEqual(water.color, color.blue)
                self.assertEqual(water.scale, (1, 0.1, 1))

    def test_cave_generation(self):
        for z in range(5, 15):
            for x in range(5, 15):
                cave = Cave(position=(x, 2, z))
                self.assertEqual(cave.color, color.black)

if __name__ == '__main__':
    unittest.main()
