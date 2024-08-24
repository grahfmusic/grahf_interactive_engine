
import pyglet
from game_elements import GameCharacter, Camera
from speech_system import SpeechSystem
from fmod_manager import FMODManager
from sfx_manager import SFXManager
from video_manager import VideoManager
from layer_manager import LayerManager
from shader_manager import ShaderManager
from portrait_manager import PortraitManager
from animation_manager import AnimationManager
from dialogue_manager import DialogueManager
from tweening_manager import TweeningManager

class Room1:
    def __init__(self, window):
        self.window = window
        self.layer_manager = LayerManager()
        self.fmod_manager = FMODManager()
        self.sfx_manager = SFXManager()
        self.video_manager = VideoManager()
        self.tweening_manager = TweeningManager()
        self.camera = Camera(window)
        self.shader_manager = ShaderManager()

        # Load shaders
        self.shader_manager.load_shader('crt', 'assets/shaders/crt.vert', 'assets/shaders/crt.frag')

        # Portrait Manager
        self.portrait_manager = PortraitManager({
            "neutral": "assets/images/character_portrait_neutral.png",
            "happy": "assets/images/character_portrait_happy.png",
            "sad": "assets/images/character_portrait_sad.png"
        })

        # Animation Manager
        self.animation_manager = AnimationManager()
        self.animation_manager.load_animation("walk", "assets/images/character_walk", 0.1)
        self.character = GameCharacter(self.animation_manager.get_animation("walk"), x=100, y=100, layer=1)

        # Initialize the speech system for this room
        self.speech = SpeechSystem(self.character, 'room1', 'dialogue_files/room1_dialogue.json')

        # Play background music using FMOD
        self.fmod_manager.load_music('assets/music/room1_bg.flac')
        self.fmod_manager.set_music_volume(0.8)

        # Play environmental SFX using FMOD
        wind_sound = self.fmod_manager.load_sound('assets/sfx/wind.opus', loop=True)
        self.wind_channel = self.fmod_manager.play_sound(wind_sound)

        # Add objects to the layer manager
        self.layer_manager.add_object(self.character)

        # Tween example: move character from (100, 100) to (400, 400)
        self.tweening_manager.tween_position(self.character.sprite, (100, 100), (400, 400), 2.0)

        # Set up window events
        self.window.push_handlers(self.on_draw, self.on_resize)
        pyglet.clock.schedule_interval(self.update, 1/60)

    def on_draw(self):
        self.window.clear()
        self.camera.begin()

        # Use CRT shader
        self.shader_manager.use_shader('crt')

        self.layer_manager.draw()
        self.video_manager.draw()  # Draw video if playing
        self.speech.draw()

        # Stop using shader
        self.shader_manager.stop_shader()

        self.camera.end()

    def on_resize(self, width, height):
        self.camera.resize(width, height)

    def update(self, dt):
        self.fmod_manager.update()  # Update FMOD system
        self.tweening_manager.update(dt)  # Update tween animations
        for obj in self.layer_manager.objects:
            obj.update(dt)

    def shutdown(self):
        self.fmod_manager.shutdown()
        self.video_manager.stop_video()
