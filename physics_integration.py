from ursina import Ursina, Entity, Vec3, time, color
from ursina.prefabs.first_person_controller import FirstPersonController
import pybullet as p

class Voxel(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            model='cube',
            color=color.white,
            texture='white_cube',
            position=position
        )
        self.collider = p.createCollisionShape(p.GEOM_BOX, halfExtents=[0.5, 0.5, 0.5])
        self.body = p.createMultiBody(baseMass=1, baseCollisionShapeIndex=self.collider, basePosition=position)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position=self.position + mouse.normal)
            if key == 'right mouse down':
                p.removeBody(self.body)
                destroy(self)

    def update(self):
        pos, _ = p.getBasePositionAndOrientation(self.body)
        self.position = Vec3(*pos)

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.controller = FirstPersonController()
        self.collider = p.createCollisionShape(p.GEOM_BOX, halfExtents=[0.5, 1, 0.5])
        self.body = p.createMultiBody(baseMass=1, baseCollisionShapeIndex=self.collider, basePosition=self.controller.position)

    def update(self):
        pos, _ = p.getBasePositionAndOrientation(self.body)
        self.controller.position = Vec3(*pos)

app = Ursina()

p.connect(p.DIRECT)
p.setGravity(0, -9.81, 0)

for z in range(8):
    for x in range(8):
        Voxel(position=(x,0,z))

player = Player()

def update():
    p.stepSimulation()
    player.update()
    for entity in scene.entities:
        if isinstance(entity, Voxel):
            entity.update()

app.run()
