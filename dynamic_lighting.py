from ursina import Ursina, Entity, Light, PointLight, color, Vec3
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

class LightSource(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            model='sphere',
            color=color.yellow,
            position=position,
            scale=0.2
        )
        self.light = PointLight(parent=self, position=Vec3(0, 0, 0), color=color.yellow)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                LightSource(position=self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)

app = Ursina()

for z in range(8):
    for x in range(8):
        Voxel(position=(x,0,z))

player = FirstPersonController()

# Add a light source at the player's initial position
light = LightSource(position=(0, 2, 0))

app.run()
