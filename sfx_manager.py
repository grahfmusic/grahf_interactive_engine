
import pyglet

class SFXManager:
    def __init__(self):
        self.sfx_player = pyglet.media.Player()

    def play_sfx(self, file, volume=1.0, loop=False, pan=0.0, distance=1.0):
        sfx = pyglet.media.load(file, streaming=False)
        self.sfx_player.queue(sfx)
        self.sfx_player.volume = volume
        self.sfx_player.position = (distance, 0, 0)
        self.sfx_player.pan = pan
        self.sfx_player.loop = loop
        self.sfx_player.play()

    def stop_sfx(self):
        if self.sfx_player:
            self.sfx_player.pause()

    def set_volume(self, volume):
        if self.sfx_player:
            self.sfx_player.volume = volume
