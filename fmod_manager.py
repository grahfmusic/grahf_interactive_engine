
import fmod

class FMODManager:
    def __init__(self):
        self.system = fmod.System()
        self.system.init()

    def load_sound(self, file, loop=False):
        mode = fmod.MODE.LOOP_NORMAL if loop else fmod.MODE.DEFAULT
        sound = self.system.create_sound(file, mode)
        return sound

    def play_sound(self, sound):
        channel = self.system.play_sound(sound)
        return channel

    def stop_sound(self, channel):
        if channel.is_playing:
            channel.stop()

    def set_volume(self, channel, volume):
        channel.volume = volume

    def update(self):
        self.system.update()

    def load_music(self, file, loop=True):
        mode = fmod.MODE.LOOP_NORMAL if loop else fmod.MODE.DEFAULT
        self.music = self.system.create_sound(file, mode)
        self.music_channel = self.system.play_sound(self.music)
        self.music_channel.volume = 1.0

    def stop_music(self):
        if self.music_channel.is_playing:
            self.music_channel.stop()

    def set_music_volume(self, volume):
        if self.music_channel:
            self.music_channel.volume = volume

    def shutdown(self):
        self.system.release()

# Example Usage
if __name__ == "__main__":
    fmod_manager = FMODManager()
    sound = fmod_manager.load_sound("assets/music/track1.flac", loop=True)
    channel = fmod_manager.play_sound(sound)
    fmod_manager.set_volume(channel, 0.5)
    fmod_manager.update()
