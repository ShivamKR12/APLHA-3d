import unittest
from ursina import Ursina, Entity, Vec3, time
from ursina.prefabs.first_person_controller import FirstPersonController

class TestGameplay(unittest.TestCase):

    def setUp(self):
        self.app = Ursina()
        self.player = FirstPersonController()
        self.entities = []

    def test_smooth_controls(self):
        initial_position = self.player.position
        self.player.position += Vec3(1, 0, 0)
        self.assertNotEqual(initial_position, self.player.position)

    def test_ai_entity_response(self):
        class AIEntity(Entity):
            def __init__(self, position=(0,0,0)):
                super().__init__(
                    model='cube',
                    color=color.random_color(),
                    position=position,
                    scale=0.5
                )
                self.direction = Vec3(1, 0, 0)
                self.speed = 1

            def update(self):
                self.position += self.direction * self.speed * time.dt

        ai_entity = AIEntity(position=(0,0,0))
        self.entities.append(ai_entity)
        initial_position = ai_entity.position
        ai_entity.update()
        self.assertNotEqual(initial_position, ai_entity.position)

    def test_environmental_interactions(self):
        class Water(Entity):
            def __init__(self, position=(0,0,0)):
                super().__init__(
                    model='cube',
                    color=color.blue,
                    texture='white_cube',
                    position=position,
                    scale=(1, 0.1, 1)
                )

        water = Water(position=(0,0,0))
        self.entities.append(water)
        self.assertEqual(water.color, color.blue)

    def tearDown(self):
        for entity in self.entities:
            destroy(entity)
        destroy(self.player)
        self.app.close()

if __name__ == '__main__':
    unittest.main()
