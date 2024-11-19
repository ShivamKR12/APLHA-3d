from ursina import Ursina, Entity, color, mouse, Vec3, destroy
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

app = Ursina()

voxel_parent = Entity()

for z in range(8):
    for x in range(8):
        Voxel(position=(x,0,z), parent=voxel_parent)

player = FirstPersonController()
app.run()
