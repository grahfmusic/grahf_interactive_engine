
import pyglet

class GameCharacter:
    def __init__(self, image, x, y, layer=0):
        self.image = pyglet.image.load(image)
        self.sprite = pyglet.sprite.Sprite(self.image, x=x, y=y)
        self.layer = layer

    def draw(self):
        self.sprite.draw()

    def update(self, dt):
        pass  # Add character-specific updates here
