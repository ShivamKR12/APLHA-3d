from ursina import Ursina, Entity, Vec3, time
from ursina.prefabs.first_person_controller import FirstPersonController

class Voxel(Entity):
    def __init__(self, position=(0,0,0), color=color.white):
        super().__init__(
            model='cube',
            color=color,
            texture='white_cube',
            position=position
        )
        self.velocity = Vec3(0, 0, 0)

    def update(self):
        self.velocity.y -= 9.81 * time.dt  # Apply gravity
        self.position += self.velocity * time.dt

        # Collision detection with ground
        if self.position.y < 0:
            self.position.y = 0
            self.velocity.y = 0

class PhysicsWorld(Entity):
    def __init__(self):
        super().__init__()
        self.voxels = []

    def add_voxel(self, voxel):
        self.voxels.append(voxel)

    def update(self):
        for voxel in self.voxels:
            voxel.update()

app = Ursina()

physics_world = PhysicsWorld()

for z in range(8):
    for x in range(8):
        voxel = Voxel(position=(x, 0, z))
        physics_world.add_voxel(voxel)

player = FirstPersonController()

def update():
    physics_world.update()

app.run()
