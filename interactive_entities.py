from ursina import Ursina, Entity, color, Vec3, time
from ursina.prefabs.first_person_controller import FirstPersonController
import random

class NPC(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            model='cube',
            color=color.random_color(),
            position=position,
            scale=0.5
        )
        self.direction = Vec3(random.uniform(-1, 1), 0, random.uniform(-1, 1)).normalized()
        self.speed = 1

    def update(self):
        self.position += self.direction * self.speed * time.dt
        if abs(self.position.x) > 10 or abs(self.position.z) > 10:
            self.direction = -self.direction

class CollectableItem(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            model='sphere',
            color=color.gold,
            position=position,
            scale=0.2
        )

class Hazard(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            model='cube',
            color=color.red,
            position=position,
            scale=0.5
        )

class Animal(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            model='cube',
            color=color.brown,
            position=position,
            scale=0.5
        )
        self.direction = Vec3(random.uniform(-1, 1), 0, random.uniform(-1, 1)).normalized()
        self.speed = 0.5

    def update(self):
        self.position += self.direction * self.speed * time.dt
        if abs(self.position.x) > 10 or abs(self.position.z) > 10:
            self.direction = -self.direction

app = Ursina()

for z in range(8):
    for x in range(8):
        Entity(model='cube', color=color.green, position=(x,0,z))

player = FirstPersonController()

# Add NPCs
for _ in range(5):
    NPC(position=(random.uniform(-10, 10), 0, random.uniform(-10, 10)))

# Add collectable items
for _ in range(10):
    CollectableItem(position=(random.uniform(-10, 10), 0, random.uniform(-10, 10)))

# Add hazards
for _ in range(3):
    Hazard(position=(random.uniform(-10, 10), 0, random.uniform(-10, 10)))

# Add animals
for _ in range(5):
    Animal(position=(random.uniform(-10, 10), 0, random.uniform(-10, 10)))

app.run()
