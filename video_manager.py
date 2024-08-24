
import pyglet

class VideoManager:
    def __init__(self):
        self.current_video = None

    def play_video(self, file, loop=False, play_audio=True):
        self.current_video = pyglet.media.load(file)
        self.video_player = pyglet.media.Player()
        self.video_player.queue(self.current_video)
        self.video_player.loop = loop
        self.video_player.volume = 1.0 if play_audio else 0.0
        self.video_player.play()

    def stop_video(self):
        if self.video_player:
            self.video_player.pause()

    def set_volume(self, volume):
        if self.video_player:
            self.video_player.volume = volume

    def draw(self):
        if self.video_player and self.video_player.source:
            self.video_player.get_texture().blit(0, 0)
