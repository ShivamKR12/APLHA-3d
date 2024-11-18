import unittest
from ursina import Ursina, Entity, Vec3, time
from ursina.prefabs.first_person_controller import FirstPersonController

class TestStress(unittest.TestCase):

    def setUp(self):
        self.app = Ursina()
        self.player = FirstPersonController()
        self.entities = []

    def test_extreme_player_movement_speeds(self):
        initial_position = self.player.position
        self.player.position += Vec3(1000, 0, 0)
        self.assertNotEqual(initial_position, self.player.position)

    def test_large_scale_world_exploration(self):
        initial_position = self.player.position
        for _ in range(1000):
            self.player.position += Vec3(1, 0, 0)
        self.assertNotEqual(initial_position, self.player.position)

    def test_high_density_block_placement(self):
        class Voxel(Entity):
            def __init__(self, position=(0,0,0)):
                super().__init__(
                    model='cube',
                    color=color.white,
                    texture='white_cube',
                    position=position
                )

        for z in range(100):
            for x in range(100):
                voxel = Voxel(position=(x,0,z))
                self.entities.append(voxel)
        self.assertEqual(len(self.entities), 10000)

    def test_multiplayer_performance(self):
        class Player(Entity):
            def __init__(self, position=(0,0,0)):
                super().__init__(
                    model='cube',
                    color=color.random_color(),
                    position=position,
                    scale=0.5
                )

        players = [Player(position=(i,0,0)) for i in range(10)]
        self.entities.extend(players)
        self.assertEqual(len(self.entities), 10)

    def test_synchronization_and_latency(self):
        class Player(Entity):
            def __init__(self, position=(0,0,0)):
                super().__init__(
                    model='cube',
                    color=color.random_color(),
                    position=position,
                    scale=0.5
                )

        players = [Player(position=(i,0,0)) for i in range(10)]
        self.entities.extend(players)
        initial_positions = [player.position for player in players]
        for player in players:
            player.position += Vec3(1, 0, 0)
        for initial_position, player in zip(initial_positions, players):
            self.assertNotEqual(initial_position, player.position)

    def tearDown(self):
        for entity in self.entities:
            destroy(entity)
        destroy(self.player)
        self.app.close()

if __name__ == '__main__':
    unittest.main()
