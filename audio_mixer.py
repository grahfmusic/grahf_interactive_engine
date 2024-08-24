
from pyo import *

class AudioMixer:
    def __init__(self):
        self.server = Server().boot().start()
        self.music_volume = Sig(0.5)
        self.sfx_volume = Sig(0.5)
        self.speech_volume = Sig(0.5)

    def play_music(self, file, loop=True):
        self.stop_music()
        self.music_stream = SfPlayer(file, loop=loop, mul=self.music_volume).out()

    def stop_music(self):
        if hasattr(self, 'music_stream'):
            self.music_stream.stop()

    def play_sfx(self, file, loop=False):
        self.stop_sfx()
        self.sfx_stream = SfPlayer(file, loop=loop, mul=self.sfx_volume).out()

    def stop_sfx(self):
        if hasattr(self, 'sfx_stream'):
            self.sfx_stream.stop()

    def play_speech(self, file, loop=False):
        self.stop_speech()
        self.speech_stream = SfPlayer(file, loop=loop, mul=self.speech_volume).out()

    def stop_speech(self):
        if hasattr(self, 'speech_stream'):
            self.speech_stream.stop()

    def set_music_volume(self, volume):
        self.music_volume.value = volume

    def set_sfx_volume(self, volume):
        self.sfx_volume.value = volume

    def set_speech_volume(self, volume):
        self.speech_volume.value = volume

    def apply_reverb(self, room_size=0.5, damping=0.5, wet=0.3):
        self.music_stream = STRev(self.music_stream, inpos=0.5, revtime=room_size, cutoff=damping, bal=wet).out()

    def apply_echo(self, delay_time=0.5, feedback=0.3):
        self.music_stream = Delay(self.music_stream, delay=delay_time, feedback=feedback).out()

    def apply_filter(self, cutoff_freq, filter_type='low'):
        if filter_type == 'low':
            self.music_stream = ButLP(self.music_stream, freq=cutoff_freq).out()
        elif filter_type == 'high':
            self.music_stream = ButHP(self.music_stream, freq=cutoff_freq).out()

    def apply_panning(self, pan=0.5):
        self.music_stream = Pan(self.music_stream, outs=2, pan=pan).out()

    def stop_all(self):
        self.stop_music()
        self.stop_sfx()
        self.stop_speech()

    def shutdown(self):
        self.server.stop()
        self.server.shutdown()
