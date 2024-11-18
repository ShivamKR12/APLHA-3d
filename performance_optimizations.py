from ursina import Ursina, Entity, color, Vec3
from ursina.prefabs.first_person_controller import FirstPersonController
from multiprocessing import Process, Queue
import time

class Voxel(Entity):
    def __init__(self, position=(0,0,0), color=color.white):
        super().__init__(
            model='cube',
            color=color,
            texture='white_cube',
            position=position
        )

class Chunk(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__()
        self.position = position
        self.voxels = []

    def generate_voxels(self, queue):
        for z in range(8):
            for x in range(8):
                voxel = Voxel(position=(x,0,z))
                self.voxels.append(voxel)
        queue.put(self.voxels)

class World(Entity):
    def __init__(self):
        super().__init__()
        self.chunks = []
        self.queue = Queue()

    def generate_chunk(self, position):
        chunk = Chunk(position=position)
        process = Process(target=chunk.generate_voxels, args=(self.queue,))
        process.start()
        self.chunks.append(chunk)

    def update(self):
        while not self.queue.empty():
            voxels = self.queue.get()
            for voxel in voxels:
                voxel.parent = self

app = Ursina()

world = World()
world.generate_chunk(position=(0,0,0))

player = FirstPersonController()

def update():
    world.update()

app.run()
