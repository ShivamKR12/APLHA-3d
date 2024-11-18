from ursina import Ursina, Audio, Entity, color, Vec3, time
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
                Audio('block_place.wav').play()
            if key == 'right mouse down':
                destroy(self)
                Audio('block_break.wav').play()

class AmbientMusic(Entity):
    def __init__(self):
        super().__init__()
        self.audio = Audio('ambient_music.mp3', loop=True, autoplay=True)

class DynamicAudioSystem(Entity):
    def __init__(self):
        super().__init__()
        self.current_biome = 'forest'
        self.day_time = 0
        self.audio = Audio('forest_day.mp3', loop=True, autoplay=True)

    def update(self):
        self.day_time += time.dt * 0.1
        if self.day_time % 1 < 0.5:
            if self.current_biome == 'forest':
                self.audio.clip = 'forest_day.mp3'
            elif self.current_biome == 'desert':
                self.audio.clip = 'desert_day.mp3'
        else:
            if self.current_biome == 'forest':
                self.audio.clip = 'forest_night.mp3'
            elif self.current_biome == 'desert':
                self.audio.clip = 'desert_night.mp3'
        self.audio.play()

app = Ursina()

for z in range(8):
    for x in range(8):
        Voxel(position=(x,0,z))

player = FirstPersonController()

# Add ambient background music
ambient_music = AmbientMusic()

# Add dynamic audio system
dynamic_audio_system = DynamicAudioSystem()

app.run()
