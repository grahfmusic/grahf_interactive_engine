
import pyglet
from pyglet.math import Vec2

class Tween:
    def __init__(self, start, end, duration, update_func, on_complete=None):
        self.start = start
        self.end = end
        self.duration = duration
        self.update_func = update_func
        self.on_complete = on_complete
        self.elapsed = 0

    def update(self, dt):
        self.elapsed += dt
        t = min(self.elapsed / self.duration, 1)
        value = self.start + (self.end - self.start) * t
        self.update_func(value)

        if t == 1 and self.on_complete:
            self.on_complete()

class TweeningManager:
    def __init__(self):
        self.tweens = []

    def tween_position(self, sprite, start, end, duration):
        def update_func(pos):
            sprite.x, sprite.y = pos.x, pos.y
        tween = Tween(Vec2(*start), Vec2(*end), duration, update_func)
        self.tweens.append(tween)

    def tween_scale(self, sprite, start, end, duration):
        def update_func(scale):
            sprite.scale = scale
        tween = Tween(start, end, duration, update_func)
        self.tweens.append(tween)

    def update(self, dt):
        for tween in self.tweens[:]:
            tween.update(dt)
            if tween.elapsed >= tween.duration:
                self.tweens.remove(tween)
