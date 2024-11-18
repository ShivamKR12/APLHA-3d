from ursina import Ursina, Entity, Sky, time, Vec3, color, ParticleSystem, Particle

class DayNightCycle(Entity):
    def __init__(self):
        super().__init__()
        self.sky = Sky()
        self.day_time = 0

    def update(self):
        self.day_time += time.dt * 0.1
        self.sky.rotation_y = self.day_time * 360
        self.sky.color = color.rgb(255, 255, 255) if self.day_time % 1 < 0.5 else color.rgb(0, 0, 0)

class WeatherSystem(Entity):
    def __init__(self):
        super().__init__()
        self.weather_type = 'clear'
        self.particle_system = ParticleSystem()

    def set_weather(self, weather_type):
        self.weather_type = weather_type
        if weather_type == 'rain':
            self.particle_system = ParticleSystem(
                Particle(
                    model='quad',
                    color=color.blue,
                    scale=0.1,
                    position=Vec3(0, 10, 0),
                    velocity=Vec3(0, -1, 0)
                )
            )
        elif weather_type == 'snow':
            self.particle_system = ParticleSystem(
                Particle(
                    model='quad',
                    color=color.white,
                    scale=0.1,
                    position=Vec3(0, 10, 0),
                    velocity=Vec3(0, -0.5, 0)
                )
            )
        elif weather_type == 'fog':
            self.particle_system = ParticleSystem(
                Particle(
                    model='quad',
                    color=color.gray,
                    scale=0.1,
                    position=Vec3(0, 10, 0),
                    velocity=Vec3(0, -0.1, 0)
                )
            )
        else:
            self.particle_system.clear()

class BlockParticleEffect(Entity):
    def __init__(self, position):
        super().__init__()
        self.particle_system = ParticleSystem(
            Particle(
                model='cube',
                color=color.random_color(),
                scale=0.1,
                position=position,
                velocity=Vec3(0, 1, 0)
            )
        )

app = Ursina()

day_night_cycle = DayNightCycle()
weather_system = WeatherSystem()

def update():
    day_night_cycle.update()
    weather_system.particle_system.update()

app.run()
