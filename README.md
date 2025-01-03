# Basic 3D Voxel Game in Python

## Project Setup

1. Initialize a new Python project and set up a virtual environment.
2. Install dependencies:
   ```bash
   pip install ursina
   ```
3. Create a `main.py` file to serve as the entry point.

## Game Framework

1. Set up the game window using Ursina.
2. Create a basic player controller with first-person movement.

## Voxel System

1. Implement a voxel class to represent blocks in the world.
2. Define basic voxel properties, such as size, color, and texture.

## Terrain Generation

1. Use procedural generation to create a flat or hilly terrain.
2. Optional: Integrate noise functions (e.g., Perlin or Simplex noise) for more realistic terrain.

## Block Interaction

1. Add functionality to place and remove blocks using the mouse.
2. Highlight the targeted block for better interaction feedback.

## Physics and Collision

1. Integrate basic collision detection to prevent the player from walking through blocks or falling out of the terrain.
2. Ensure smooth movement across the terrain.

## Lighting and Shading

1. Add ambient lighting and shadows for a more immersive experience.
2. Optional: Implement a day-night cycle.

## Game Optimization

1. Implement greedy meshing for voxel optimization to reduce the number of drawn faces.
2. Integrate chunk-based rendering for performance improvements in larger worlds.

## Save and Load System

1. Allow saving the current state of the world (e.g., blocks placed/removed) to a file.
2. Implement a loading system to restore the saved world.

## Enhancements (Optional)

1. Add textures to blocks for better visual quality.
2. Introduce additional block types (e.g., dirt, stone, water).
3. Add player tools or inventory for block management.

## Block Interaction Details

### Placing and Removing Blocks

- **Placing Blocks**: To place a block, hover over an existing block and press the left mouse button. A new block will be placed adjacent to the existing block in the direction you are facing.
- **Removing Blocks**: To remove a block, hover over the block you want to remove and press the right mouse button. The block will be removed from the world.

### Code Example

Here is an example of how block interaction is implemented in the `main.py` file:

```python
from ursina import Ursina, Entity, color, mouse
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

for z in range(8):
    for x in range(8):
        Voxel(position=(x,0,z))

player = FirstPersonController()
app.run()
```

This code sets up a basic voxel world where you can place and remove blocks using the mouse.

## Running the Game

To run the game, execute the `main.py` file:

```bash
python main.py
```

## Game Features

- **Player Movement**: Move around the world using the WASD keys and mouse for looking around.
- **Block Placement and Removal**: Place and remove blocks using the left and right mouse buttons.
- **Procedurally Generated Terrain**: Explore a flat or hilly terrain generated procedurally.

## Testing Structure and Test Cases

### Testing Structure

The repository includes a dedicated testing structure for unit and integration tests. The tests are organized into different categories to ensure comprehensive coverage of all critical game features and components.

### Test Cases

1. **Unit Tests**
   - Test individual components like voxels, player controls, and terrain generation.
   - Verify that all parameters produce the expected results, such as block placement, removal, and chunk handling.
   - Ensure that error handling works as intended for invalid inputs.

2. **Integration Tests**
   - Check the interaction between components like player actions, crafting systems, and entity behavior.
   - Test game mechanics, such as crafting recipes, block durability, and resource collection.
   - Ensure transitions between game states, such as loading new chunks or saving progress, function seamlessly.

3. **Performance Tests**
   - Assess chunk loading and rendering performance in different scenarios, such as dense terrain or high-speed movement.
   - Test the impact of dynamic lighting, weather effects, and particle systems on frame rates.
   - Identify potential bottlenecks in terrain generation or physics simulations.

4. **Gameplay Tests**
   - Playtest the game to ensure smooth controls, proper collision detection, and expected gameplay behavior.
   - Verify that AI entities respond appropriately to player actions and environmental changes.
   - Ensure all environmental interactions, such as fire spreading or water flowing, behave realistically.

5. **Stress Tests**
   - Simulate edge cases, such as extreme player movement speeds, large-scale world exploration, or high-density block placement.
   - Test multiplayer performance by connecting multiple players and observing synchronization and latency.

6. **Bug Tracking**
   - Document any bugs or inconsistencies discovered during testing.
   - Prioritize fixes based on their impact on gameplay and stability.
   - Retest resolved issues to ensure they are fully addressed.

7. **Final Review**
   - Perform a comprehensive review of the game to confirm all features are functional and optimized.
   - Ensure the game meets performance benchmarks and runs smoothly on intended platforms.

## Running the Tests

To run the tests, execute the following command:

```bash
python -m unittest discover tests
```

This command will discover and run all the test cases in the `tests` directory.

## Importance of Testing

Testing is a crucial part of the development process to ensure that all components of the game function correctly and meet performance expectations. By thoroughly testing the game, we can identify and fix issues early, leading to a more stable and enjoyable gaming experience.

## VNC Setup

To set up a VNC server in a separate directory outside the main game directory, follow these steps:

1. **Create a new directory for VNC setup:**

   ```bash
   mkdir -p ~/vnc_setup
   cd ~/vnc_setup
   ```

2. **Install VNC server:**

   ```bash
   sudo apt update
   sudo apt install -y tightvncserver
   ```

3. **Configure VNC server:**

   - Start the VNC server to set up a password:

     ```bash
     vncserver
     ```

   - Kill the VNC server instance:

     ```bash
     vncserver -kill :1
     ```

   - Create a VNC configuration file:

     ```bash
     nano ~/.vnc/xstartup
     ```

     Add the following lines to the file:

     ```bash
     #!/bin/bash
     xrdb $HOME/.Xresources
     startxfce4 &
     ```

   - Make the file executable:

     ```bash
     chmod +x ~/.vnc/xstartup
     ```

4. **Start the VNC server:**

   ```bash
   vncserver :1
   ```

5. **Access the VNC server:**

   - Use a VNC viewer to connect to the VNC server. The address will be `your_server_ip:1`.

6. **Stop the VNC server:**

   ```bash
   vncserver -kill :1
   ```

By following these steps, you will have a VNC server set up in a separate directory outside the main game directory, running independently without causing any major connections or errors in the main files.

## VNC Viewer Setup and Connection Instructions

To connect to the VNC server using a VNC viewer, follow these steps:

1. **Install a VNC viewer on your local machine:**

   Popular options include RealVNC Viewer, TightVNC Viewer, and TigerVNC Viewer.

2. **Open the VNC viewer application on your local machine.**

3. **Enter the VNC server address:**

   Use the format `your_server_ip:1` where `your_server_ip` is the IP address of the server running the VNC server.

4. **Click the "Connect" button to initiate the connection.**

5. **Enter the VNC server password:**

   When prompted, enter the VNC server password that you set up during the VNC server configuration.

6. **View the remote desktop:**

   Once connected, you should see the remote desktop of the VNC server.

For more detailed instructions on setting up the VNC server, refer to the `vnc_setup/README.md` file in the `vnc_setup` directory.
