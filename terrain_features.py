from ursina import Ursina, Entity, color, Vec3
from perlin_noise import PerlinNoise

class Voxel(Entity):
    def __init__(self, position=(0,0,0), color=color.white):
        super().__init__(
            model='cube',
            color=color,
            texture='white_cube',
            position=position
        )

class Terrain(Entity):
    def __init__(self):
        super().__init__()
        self.noise = PerlinNoise(octaves=4, seed=2024)
        self.generate_terrain()

    def generate_terrain(self):
        for z in range(20):
            for x in range(20):
                y = self.noise([x/20, z/20]) * 10
                Voxel(position=(x, int(y), z), color=color.green)

class Water(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            model='cube',
            color=color.blue,
            texture='white_cube',
            position=position,
            scale=(1, 0.1, 1)
        )

class Cave(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            model='cube',
            color=color.black,
            texture='white_cube',
            position=position
        )

class Biome(Entity):
    def __init__(self, position=(0,0,0), biome_type='forest'):
        super().__init__(
            model='cube',
            color=color.green if biome_type == 'forest' else color.yellow if biome_type == 'desert' else color.gray,
            texture='white_cube',
            position=position
        )

class TerrainVariation(Entity):
    def __init__(self, position=(0,0,0), variation_type='cave'):
        super().__init__(
            model='cube',
            color=color.black if variation_type == 'cave' else color.brown,
            texture='white_cube',
            position=position
        )

app = Ursina()

terrain = Terrain()

# Add water blocks
for z in range(20):
    for x in range(20):
        Water(position=(x, -1, z))

# Add cave blocks
for z in range(5, 15):
    for x in range(5, 15):
        Cave(position=(x, 2, z))

# Add biomes
for z in range(20):
    for x in range(20):
        Biome(position=(x, 0, z), biome_type='forest' if (x + z) % 3 == 0 else 'desert' if (x + z) % 3 == 1 else 'mountains')

# Add terrain variations
for z in range(5, 15):
    for x in range(5, 15):
        TerrainVariation(position=(x, 3, z), variation_type='cave' if (x + z) % 2 == 0 else 'overhang')

app.run()
