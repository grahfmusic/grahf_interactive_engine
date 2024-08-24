
## GISF (Grahf Interactive Story Framework)
### Version 0.0.1 (prototype)



## 1. Introduction

### Comprehensive Overview

This ultra-detailed documentation provides a thorough guide to using the custom game framework developed in Python. This framework is designed to be highly customizable, allowing for the creation of complex, story-driven games with advanced features like real-time audio manipulation, video playback with transparency, and sophisticated animation systems.

Whether you're an experienced developer or new to game development, this documentation will walk you through every aspect of the framework, from setting up your project to implementing advanced features. Each section is filled with detailed explanations, code examples, and best practices to ensure you can make the most out of this powerful tool.

### Key Features

- **Multi-Platform Support**: Fully compatible with Linux, macOS, and Windows, allowing you to develop and deploy your game across multiple platforms with ease.
- **Advanced Audio Management**: Includes FMOD integration for managing high-quality sound effects, music, and speech, with support for multiple audio formats.
- **Robust Animation System**: Supports complex animations, including sprite sheets, tweening, and real-time updates.
- **Shader Effects**: Implement visual effects such as CRT, bloom, and more using custom shaders.
- **Comprehensive Debugging Tools**: Includes frame rate monitoring, memory usage tracking, and dynamic room loading for testing.
- **Video Playback**: Supports VP8 and VP9 video formats with transparency, along with options to control playback and mute audio.
- **Real-Time Effects**: Apply real-time effects like reverb, echo, and panning to your game's audio, enhancing the immersive experience.
- **Dynamic Resolution Handling**: Automatically adjusts to different screen resolutions, including support for ultra-widescreen formats.

### Supported Platforms and Formats

- **Operating Systems**: Linux, macOS, Windows
- **Audio Formats**: FLAC, Opus, WAV, OGG
- **Video Formats**: VP8, VP9 (with transparency support)
- **Image Formats**: PNG, JPEG (with optional compression)
- **Shader Formats**: GLSL (for vertex and fragment shaders)

## 2. Setting Up the Project

### In-Depth Directory Structure

To effectively manage your game project, it's essential to organize your files and directories in a structured manner. Below is the recommended directory structure, which separates assets, scripts, and build tools into distinct folders for easy management.

```plaintext
my_game/
├── assets/
│   ├── audio/             # Store all audio files here (music, SFX, speech)
│   ├── images/            # Store all image files here (backgrounds, sprites, UI)
│   ├── music/             # Store music files in FLAC format for high quality
│   ├── sfx/               # Store sound effects in Opus or WAV format
│   ├── shaders/           # Store shader files (e.g., CRT shader) in GLSL format
│   └── video/             # Store video files in VP8/VP9 format, supporting transparency
├── build_tools/
│   ├── compile_code.py    # Tool for compiling Python code into a standalone executable
│   ├── package_assets.py  # Tool for packaging assets with optional compression and encryption
│   ├── build.py           # Main script to automate the build process
│   ├── patch_tool.py      # Tool for applying patches to existing builds
│   ├── encryption_tool.py # Utility for encrypting assets to prevent reverse engineering
│   └── requirements.txt   # Lists all Python dependencies required for the project
├── main.py                # Main game script that initializes and runs the game
├── room1.py               # Implementation of the first room/scene in your game
├── room2.py               # Placeholder for additional rooms/scenes
├── settings.py            # Script for managing game settings (resolution, volume, etc.)
├── credits.py             # Script for displaying the credits screen
├── save_game.py           # Script for managing save and load game functionality
├── shader_manager.py      # Manages loading and applying shaders in the game
├── portrait_manager.py    # Manages character portraits, including different emotional states
├── animation_manager.py   # Manages animations, including sprite sheets and real-time updates
├── dialogue_manager.py    # Manages dialogue, including speech file generation
├── rhubarb_integration.py # Integrates Rhubarb for generating lip-sync data
├── fmod_manager.py        # Manages audio playback using FMOD
├── video_manager.py       # Manages video playback with support for transparency
├── tweening_manager.py    # Manages tweening animations for smooth transitions
└── sfx_manager.py         # Manages sound effects, including spatial audio and effects
```

### Step-by-Step Installation of Dependencies

Before you can start developing your game, you'll need to install several dependencies. These include libraries for rendering, audio management, and image manipulation. Below is a step-by-step guide to setting up your development environment.

#### Python and PIP

Ensure that Python 3.8 or higher is installed on your system. You can check your Python version by running:

```bash
python --version
```

If Python is not installed, download it from the official [Python website](https://www.python.org/).

#### Installing Dependencies

Navigate to the `build_tools` directory and install the necessary dependencies using the following command:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes essential libraries like:

- **Pyglet**: For windowing, rendering, and handling input.
- **FMOD**: For advanced audio processing and management.
- **PIL (Pillow)**: For image manipulation and processing.
- **pyo**: For additional audio processing capabilities.
- **Subprocess**: For running external processes like Rhubarb (for lip-syncing).

#### Additional Setup for FMOD

FMOD is a proprietary audio engine, so you'll need to download the FMOD API from the [FMOD website](https://www.fmod.com/). Once downloaded, extract the files and place them in the appropriate directory as indicated in your `fmod_manager.py` script.

## 3. Core Components

### Detailed Explanation of Room Management

Rooms are the core building blocks of your game. Each room represents a distinct area or scene within the game world. Managing rooms effectively allows for smooth transitions between scenes and efficient resource management.

### Room1 Example: A Step-by-Step Guide

The `Room1` class defined in `room1.py` is a template for creating new rooms in your game. Below is a detailed breakdown of how to implement and customize your own rooms.

#### Initialization

The `__init__` method is used to set up all necessary components for the room, including loading assets, setting up the camera, and initializing game objects.

```python
class Room1:
    def __init__(self, window):
        # Initialize the room's components
        self.window = window
        self.camera = Camera(window)
        self.layer_manager = LayerManager()
        self.fmod_manager = FMODManager()
        self.initialize_objects()

    def initialize_objects(self):
        # Load and place game objects in the room
        self.character = GameCharacter('assets/images/hero.png', x=100, y=150, layer=1)
        self.layer_manager.add_object(self.character)
```

#### Drawing the Room

The `on_draw` method is responsible for rendering the room. It clears the screen, sets up the camera, and draws all the objects in the room using the `LayerManager`.

```python
def on_draw(self):
    self.window.clear()
    self.camera.begin()
    self.layer_manager.draw()
    self.camera.end()
```

## 4. Advanced Features

### Tweening System

The Tweening system is used to create smooth transitions for object properties like position, scale, and opacity. This can be particularly useful for animations, camera movements, and other dynamic effects.

#### Tweening Example: Moving an Object

```python
tween_manager = TweeningManager()

# Move the character from (100, 150) to (300, 400) over 2 seconds
tween_manager.tween_position(self.character.sprite, (100, 150), (300, 400), 2.0)
```

### Shader Effects

Shader effects can greatly enhance the visual quality of your game. This framework supports custom GLSL shaders that can be applied to the entire screen or specific objects.

#### CRT Shader Example

To apply a CRT shader effect, load the shader in the `ShaderManager` and use it during the drawing process.

```python
shader_manager = ShaderManager()

# Load the CRT shader
shader_manager.load_shader('crt', 'assets/shaders/crt.vert', 'assets/shaders/crt.frag')

def on_draw(self):
    self.window.clear()
    self.camera.begin()
    shader_manager.use_shader('crt')
    self.layer_manager.draw()
    shader_manager.stop_shader()
    self.camera.end()
```

## 5. Audio and Video Support

### Audio Management with FMOD

FMOD is used for advanced audio management in this framework. It supports various formats, real-time effects, and spatial audio.

#### Playing Background Music

```python
fmod_manager = FMODManager()
fmod_manager.load_music('assets/music/background.flac')
fmod_manager.play_music()
```

### Video Playback with Transparency

This framework supports VP8 and VP9 video formats with transparency. You can control playback and manage the video layer with the `VideoManager`.

#### Playing a Transparent Video

```python
video_manager = VideoManager()
video_manager.play_video('assets/video/intro.webm', loop=False, play_audio=True)
```

## 6. Building and Packaging

### Using the Build Tools

The build tools included in this framework are designed to streamline the process of compiling your game, packaging assets, and creating standalone executables for distribution.

#### Compiling the Python Code

Use the `compile_code.py` script to compile your Python code into an executable. This script ensures that all dependencies are bundled, so players do not need to install Python separately.

```bash
python build_tools/compile_code.py
```

#### Packaging Assets

The `package_assets.py` script packages all your assets into a compressed and encrypted file. This step is crucial for protecting your game assets from being easily extracted.

```bash
python build_tools/package_assets.py
```

#### Building the Game

Finally, the `build.py` script automates the entire process, including compiling the code, packaging assets, and preparing the final build for distribution.

```bash
python build_tools/build.py
```

## 7. Examples and Usage

### Implementing a New Room

Creating a new room in your game is straightforward with this framework. Each room is typically represented by a separate Python file. Below is an example of how to implement a new room:

```python
from camera import Camera
from layer_manager import LayerManager
from fmod_manager import FMODManager
from game_character import GameCharacter

class Room2:
    def __init__(self, window):
        self.window = window
        self.camera = Camera(window)
        self.layer_manager = LayerManager()
        self.fmod_manager = FMODManager()
        self.initialize_objects()

    def initialize_objects(self):
        self.character = GameCharacter('assets/images/hero.png', x=50, y=100, layer=1)
        self.layer_manager.add_object(self.character)

    def on_draw(self):
        self.window.clear()
        self.camera.begin()
        self.layer_manager.draw()
        self.camera.end()

    def update(self, dt):
        self.layer_manager.update(dt)

    def handle_input(self, key):
        if key == 'w':
            self.character.move_up()
        elif key == 's':
            self.character.move_down()
        elif key == 'a':
            self.character.move_left()
        elif key == 'd':
            self.character.move_right()
```

### Adding New Animations

Animations can be added to any game object using the `AnimationManager`. Below is an example of how to add a walking animation to a character:

```python
from animation_manager import AnimationManager

animation_manager = AnimationManager()

# Load a walking animation
animation_manager.load_animation('walk', 'assets/animations/walk/', loop=True)

# Assign the animation to the character
self.character.set_animation('walk')
```

### Managing Dialogue with JSON

Dialogue can be managed using JSON files, which are then processed by the `DialogueManager`. Here is an example of a JSON file for dialogue and how to load it:

#### dialogue_room1.json

```json
{
    "dialogues": [
        {
            "character": "hero",
            "lines": [
                "Welcome to our adventure!",
                "Let's explore this world together."
            ]
        },
        {
            "character": "sidekick",
            "lines": [
                "I can't wait to see what's out there.",
                "Don't forget to save your progress!"
            ]
        }
    ]
}
```

#### Loading the Dialogue

```python
from dialogue_manager import DialogueManager

dialogue_manager = DialogueManager('assets/dialogue/dialogue_room1.json')

# Play the first line of dialogue
dialogue_manager.play_line('hero', 0)
```

## 8. Debugging and Testing

### Debug Functions

The framework includes a variety of debug functions to help you test and optimize your game. These functions can be accessed during development to monitor performance and adjust game parameters.

#### Example: Displaying Frame Rate

```python
from debug_manager import DebugManager

debug_manager = DebugManager()

def on_draw(self):
    self.window.clear()
    self.camera.begin()
    self.layer_manager.draw()
    debug_manager.display_fps()
    self.camera.end()
```

### Testing Transitions

Testing transitions between rooms is crucial for ensuring smooth gameplay. Use the following method to switch between rooms:

```python
def change_room(self, new_room):
    self.current_room = new_room
    self.current_room.on_draw()
```

## 9. Conclusion

### Best Practices

To make the most out of this game framework, consider the following best practices:

- **Organize Assets Effectively**: Keep your assets well-organized in their respective directories. This makes it easier to manage and update your project.
- **Use JSON for Dialogue**: Managing dialogue and other dynamic content with JSON files allows for easier updates and localization.
- **Regularly Use Debug Tools**: Utilize the built-in debug tools frequently to monitor performance, especially frame rate and memory usage.
- **Optimize for Multiple Resolutions**: Test your game on different resolutions, including ultra-widescreen formats, to ensure a consistent experience across devices.
- **Leverage Shaders for Effects**: Use custom GLSL shaders to enhance the visual quality of your game, but ensure they are optimized for performance.

### Extending the Framework

This framework is designed to be extensible. You can add new features, integrate additional libraries, or modify existing components to suit your needs. Consider the following areas for extension:

- **Additional Audio Effects**: Integrate more advanced audio effects by extending the `FMODManager`.
- **Custom UI Elements**: Create custom UI components by extending the `LayerManager` and `AnimationManager`.
- **Networked Multiplayer**: Add networked multiplayer support by integrating libraries like `socketio` or `websockets`.

### Community and Support

If you encounter any issues or have questions, consider the following resources:

- **GitHub Issues**: Report bugs or request features on the project's GitHub page.
- **Community Forums**: Participate in game development forums to get advice and share your experiences.
- **Documentation**: Always refer back to this documentation for detailed instructions and examples.

## 10. License

This game framework is licensed under the MIT License. You are free to use, modify, and distribute this framework in your projects. Please see the `LICENSE` file for more details.

## 11. Building Tools

### Compiling the Game

To compile your Python game code into a standalone executable, use the `compile_code.py` script. This ensures that all dependencies are bundled, making it easy to distribute your game without requiring players to install Python separately.

```bash
python build_tools/compile_code.py
```

### Packaging Assets

The `package_assets.py` script is used to compress and encrypt your game assets. This step is crucial for protecting your game’s assets from being easily extracted.

```bash
python build_tools/package_assets.py
```

### Automating the Build Process

The `build.py` script automates the entire build process, including compiling the code and packaging assets. This is the final step before distributing your game.

```bash
python build_tools/build.py
```

## 12. Tweening System

### Introduction to Tweening

Tweening is a powerful tool for creating smooth transitions in your game. It can be used to animate properties such as position, scale, and opacity over time.

### Example: Moving an Object

```python
tween_manager = TweeningManager()

# Move the character from (100, 150) to (300, 400) over 2 seconds
tween_manager.tween_position(self.character.sprite, (100, 150), (300, 400), 2.0)
```

### Advanced Tweening

You can chain multiple tweens together or create custom easing functions to control the acceleration and deceleration of animations.

## 13. Animations

### Creating Animations with Sprite Sheets

Animations in this framework are managed by the `AnimationManager`. Sprite sheets are the most common way to manage animations. Here's how to load and use them:

```python
animation_manager = AnimationManager()

# Load a walking animation
animation_manager.load_animation('walk', 'assets/animations/walk/', loop=True)

# Assign the animation to the character
self.character.set_animation('walk')
```

### Custom Animations

In addition to sprite sheets, you can create custom animations by manually defining frames and transitions. This allows for complex animations like particle effects or UI animations.

## 14. Audio Management with FMOD

### Loading and Playing Audio

FMOD is a powerful audio engine that allows for advanced audio manipulation. Here's how to load and play background music:

```python
fmod_manager = FMODManager()
fmod_manager.load_music('assets/music/background.flac')
fmod_manager.play_music()
```

### Sound Effects and Speech

You can also manage sound effects and speech using FMOD. This includes real-time audio effects like reverb and echo, which can be applied dynamically based on the game environment.

## 15. Load/Save Functionality

### Implementing Save and Load

The framework includes built-in support for saving and loading game progress. This is done by serializing the game state (e.g., current room, player position, inventory) into a file.

```python
save_manager = SaveManager()

# Save the current game state
save_manager.save_game('save1.dat')

# Load a saved game state
save_manager.load_game('save1.dat')
```

### Autosaving

You can also implement autosave functionality by calling the `save_game` method at regular intervals or key points in the game.

## 16. Game Settings and Menu Creation

### Creating a Settings Menu

Settings are managed through the `SettingsManager`. You can allow players to adjust options like screen resolution, volume, and control settings.

```python
settings_manager = SettingsManager()

# Set up available resolutions
settings_manager.add_resolution(1920, 1080)
settings_manager.add_resolution(2560, 1440)

# Toggle fullscreen mode
settings_manager.set_fullscreen(True)
```

### Building the Main Menu

The main menu is the first screen players see. It typically includes options like "New Game," "Load Game," "Settings," and "Quit." You can create this menu using the `MenuManager`.

```python
menu_manager = MenuManager()

# Add menu items
menu_manager.add_item("New Game", start_new_game)
menu_manager.add_item("Load Game", load_game)
menu_manager.add_item("Settings", show_settings)
menu_manager.add_item("Quit", quit_game)

# Display the menu
menu_manager.show()
```

## 17. Integration with Rhubarb for Lip-Syncing

### Using Rhubarb for Lip-Syncing

Rhubarb is a tool for generating lip-sync animations based on dialogue audio. This framework integrates with Rhubarb to automate the lip-sync process.

```bash
rhubarb assets/speech/hero_line1.wav -o assets/lipsync/hero_line1.json
```

### Loading Lip-Sync Data

Once the lip-sync data is generated, you can use it to animate character portraits during dialogue.

```python
portrait_manager = PortraitManager()
portrait_manager.load_lip_sync('hero', 'assets/lipsync/hero_line1.json')
```

## 18. Managing Dialogue with JSON

### Structuring Dialogue with JSON

Dialogue in your game can be structured using JSON files. This allows for easy editing and localization.

#### Example JSON Structure

```json
{
    "dialogues": [
        {
            "character": "hero",
            "lines": [
                "Welcome to our adventure!",
                "Let's explore this world together."
            ]
        },
        {
            "character": "sidekick",
            "lines": [
                "I can't wait to see what's out there.",
                "Don't forget to save your progress!"
            ]
        }
    ]
}
```

### Loading and Playing Dialogue

The `DialogueManager` is responsible for loading and managing dialogue in the game.

```python
dialogue_manager = DialogueManager('assets/dialogue/dialogue_room1.json')

# Play the first line of dialogue
dialogue_manager.play_line('hero', 0)
```

## 11. Building Tools

The framework includes several tools to help streamline the process of building, packaging, and distributing your game.

### Compiling Python Code

Use the `compile_code.py` script to compile your Python code into a standalone executable. This ensures that all necessary dependencies are included, and players do not need to install Python separately.

```bash
python build_tools/compile_code.py
```

### Packaging Assets

The `package_assets.py` script compresses and encrypts your game assets into a single package. This protects your assets from being easily extracted and reduces the game's size.

```bash
python build_tools/package_assets.py
```

### Full Build Process

The `build.py` script automates the compilation, packaging, and final build creation, making it easy to prepare your game for distribution.

```bash
python build_tools/build.py
```

## 12. Tweening

Tweening is used to create smooth transitions between different values over time. The `TweeningManager` allows you to tween properties like position, scale, and rotation.

### Tweening Example: Scaling an Object

```python
tween_manager = TweeningManager()

# Scale the character from 1.0 to 2.0 over 3 seconds
tween_manager.tween_scale(self.character.sprite, 1.0, 2.0, 3.0)
```

## 13. Animations

Animations bring your game characters and objects to life. The `AnimationManager` handles loading and playing animations.

### Adding an Animation

Animations are usually stored as a series of images in a directory. The `AnimationManager` can load these images and create an animation.

```python
animation_manager = AnimationManager()

# Load a walking animation
animation_manager.load_animation('walk', 'assets/animations/walk/', loop=True)

# Assign the animation to the character
self.character.set_animation('walk')
```

## 14. Audio with FMOD

FMOD is a powerful audio engine integrated into the framework to handle sound effects, music, and voice acting.

### Loading and Playing Sound Effects

```python
fmod_manager = FMODManager()

# Load a sound effect
fmod_manager.load_sfx('jump', 'assets/sfx/jump.wav')

# Play the sound effect
fmod_manager.play_sfx('jump')
```

### Music and Ambiance

FMOD also supports playing music and ambient sounds that loop seamlessly.

```python
fmod_manager.load_music('background', 'assets/music/ambient.flac')
fmod_manager.play_music('background', loop=True)
```

## 15. Saving and Loading Games

The framework includes a `SaveGameManager` for handling game saves. This allows you to save the player's progress and load it later.

### Saving a Game

```python
save_manager = SaveGameManager()

# Save the current game state
save_manager.save_game('save1')
```

### Loading a Game

```python
save_manager.load_game('save1')
```

## 16. Settings Management

Game settings, such as resolution, volume, and control mappings, are managed by the `SettingsManager`.

### Changing Resolution

```python
settings_manager.set_resolution(1920, 1080)
```

### Adjusting Volume

```python
settings_manager.set_volume('music', 0.8)
```

## 17. Main Menu

The framework includes a simple menu system that you can customize to fit your game. The menu typically includes options like New Game, Load Game, Settings, and Quit.

### Creating a Menu

```python
menu = Menu()
menu.add_option('New Game', start_new_game)
menu.add_option('Load Game', load_game)
menu.add_option('Settings', open_settings)
menu.add_option('Quit', quit_game)
```

## 18. Rhubarb Lip-Sync Integration

Rhubarb is used for generating lip-sync data for character dialogue. This allows characters' mouths to move in sync with spoken lines.

### Generating Lip-Sync Data

```bash
rhubarb --metadata -o output.json assets/voice/line1.wav
```

### Using Lip-Sync Data in the Game

```python
lip_sync_manager = LipSyncManager()

# Load the lip-sync data
lip_sync_manager.load_sync_data('output.json')

# Sync character mouth movement with audio
lip_sync_manager.sync_with_audio('line1')
```

## 19. JSON for Dialogue and Settings

JSON files are used for managing dialogue, settings, and other dynamic content in the game. This format is easy to edit and allows for localization.

### Dialogue JSON Example

```json
{
    "dialogues": [
        {
            "character": "hero",
            "lines": [
                "Welcome to our adventure!",
                "Let's explore this world together."
            ]
        }
    ]
}
```

### Settings JSON Example

```json
{
    "resolution": {
        "width": 1920,
        "height": 1080
    },
    "volume": {
        "music": 0.8,
        "sfx": 0.7
    }
}
```

## 20. Video Routines

The framework supports playing video files in VP8 and VP9 formats, with or without transparency. You can control video playback using the `VideoManager`.

### Playing a Video

To play a video file, use the following method:

```python
video_manager = VideoManager()

# Play a video, with optional looping and audio playback
video_manager.play_video('assets/video/intro.webm', loop=False, play_audio=True)
```

### Stopping a Video

You can stop a video at any time:

```python
video_manager.stop_video()
```

## 21. Portrait Routines

Portraits are used to display character faces during dialogue. Different portraits can represent different emotions.

### Displaying a Portrait

```python
portrait_manager = PortraitManager()

# Display a happy portrait for the hero character
portrait_manager.show_portrait('hero', 'happy', position=(50, 100))
```

### Changing Portraits

You can change the portrait based on the character's emotion:

```python
portrait_manager.change_portrait('hero', 'angry')
```

### Hiding a Portrait

```python
portrait_manager.hide_portrait('hero')
```

## 22. Speech Files

Speech files are used to play voice lines during dialogue. These files are typically in Opus format for efficient compression.

### Playing a Speech File

```python
speech_manager = SpeechManager()

# Play a speech file for the hero character
speech_manager.play_speech('hero', 'assets/speech/hero_intro.opus')
```

### Stopping a Speech File

```python
speech_manager.stop_speech()
```

## 23. Character Information

Characters in your game are represented by the `GameCharacter` class. Each character can have different attributes such as position, animations, and interactions.

### Creating a Character

```python
hero = GameCharacter('assets/images/hero.png', x=100, y=150)

# Set initial health and speed
hero.set_health(100)
hero.set_speed(5)
```

### Moving a Character

Characters can move based on input or predefined paths:

```python
hero.move_to(300, 400)
```

### Character Interactions

You can define interactions between characters and objects in the game:

```python
hero.interact_with(door)
```

## 24. Sprite Information

Sprites are the 2D images used to represent characters, objects, and other elements in the game.

### Loading a Sprite

```python
sprite = Sprite('assets/images/hero.png', position=(100, 150))
```

### Animating a Sprite

You can animate a sprite using the `AnimationManager`:

```python
animation_manager.set_animation(sprite, 'walk')
```

### Changing Sprite Attributes

Attributes like position, scale, and rotation can be adjusted:

```python
sprite.set_position(200, 250)
sprite.set_scale(1.5)
sprite.set_rotation(45)
```

## 25. Sprite Sheet Information

Sprite sheets contain multiple frames of animation in a single image file. The framework can slice these sheets to animate characters and objects.

### Creating a Sprite Sheet Animation

```python
sprite_sheet = SpriteSheet('assets/spritesheets/hero_walk.png', frame_width=64, frame_height=64)

# Create an animation from the sprite sheet
animation = Animation(sprite_sheet, start_frame=0, end_frame=5, loop=True)

# Apply the animation to the character
hero.set_animation(animation)
```

### Adjusting Frame Rate

You can control the speed of the animation by adjusting the frame rate:

```python
animation.set_frame_rate(10)  # 10 frames per second
```
