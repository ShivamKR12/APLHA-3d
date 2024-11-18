import unittest
from ursina import Ursina, Entity, time
from performance_optimizations import World

class TestPerformance(unittest.TestCase):

    def setUp(self):
        self.app = Ursina()
        self.world = World()

    def test_chunk_loading_performance(self):
        start_time = time.time()
        self.world.generate_chunk(position=(0,0,0))
        end_time = time.time()
        loading_time = end_time - start_time
        self.assertLess(loading_time, 1, "Chunk loading took too long")

    def test_rendering_performance(self):
        start_time = time.time()
        for _ in range(100):
            self.world.generate_chunk(position=(0,0,0))
        end_time = time.time()
        rendering_time = end_time - start_time
        self.assertLess(rendering_time, 5, "Rendering took too long")

    def test_dynamic_lighting_performance(self):
        from dynamic_lighting import LightSource
        start_time = time.time()
        for _ in range(100):
            LightSource(position=(0, 2, 0))
        end_time = time.time()
        lighting_time = end_time - start_time
        self.assertLess(lighting_time, 2, "Dynamic lighting took too long")

    def test_weather_effects_performance(self):
        from environmental_effects import WeatherSystem
        weather_system = WeatherSystem()
        start_time = time.time()
        weather_system.set_weather('rain')
        end_time = time.time()
        weather_time = end_time - start_time
        self.assertLess(weather_time, 1, "Weather effects took too long")

    def test_particle_system_performance(self):
        from environmental_effects import BlockParticleEffect
        start_time = time.time()
        for _ in range(100):
            BlockParticleEffect(position=(0, 0, 0))
        end_time = time.time()
        particle_time = end_time - start_time
        self.assertLess(particle_time, 2, "Particle system took too long")

    def test_terrain_generation_bottlenecks(self):
        start_time = time.time()
        for _ in range(100):
            self.world.generate_chunk(position=(0,0,0))
        end_time = time.time()
        generation_time = end_time - start_time
        self.assertLess(generation_time, 10, "Terrain generation bottleneck detected")

    def test_physics_simulation_bottlenecks(self):
        from physics_integration import Voxel
        start_time = time.time()
        for _ in range(100):
            Voxel(position=(0, 0, 0))
        end_time = time.time()
        physics_time = end_time - start_time
        self.assertLess(physics_time, 5, "Physics simulation bottleneck detected")

if __name__ == '__main__':
    unittest.main()
