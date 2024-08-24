
import pyglet

class PortraitManager:
    def __init__(self, image_paths):
        self.portraits = {}
        for state, path in image_paths.items():
            self.portraits[state] = pyglet.image.load(path)
        self.current_state = "neutral"

    def set_state(self, state):
        if state in self.portraits:
            self.current_state = state

    def get_current_portrait(self):
        return self.portraits[self.current_state]
