
import pyglet
import os
from PIL import Image

class AnimationManager:
    def __init__(self):
        self.animations = {}

    def load_animation(self, name, directory, frame_duration):
        frames = []
        for filename in sorted(os.listdir(directory)):
            if filename.endswith(".png"):
                image = pyglet.image.load(os.path.join(directory, filename))
                frames.append(pyglet.image.AnimationFrame(image, frame_duration))
        self.animations[name] = pyglet.image.Animation(frames)

    def get_animation(self, name):
        return self.animations.get(name)

    def generate_spritesheet(self, directory, output_file):
        images = [Image.open(os.path.join(directory, f)) for f in sorted(os.listdir(directory)) if f.endswith('.png')]
        widths, heights = zip(*(i.size for i in images))
        total_width = sum(widths)
        max_height = max(heights)
        
        spritesheet = Image.new('RGBA', (total_width, max_height))
        x_offset = 0
        for im in images:
            spritesheet.paste(im, (x_offset, 0))
            x_offset += im.size[0]
        
        spritesheet.save(output_file)

    def compress_spritesheet(self, input_file, output_file):
        image = Image.open(input_file)
        image.save(output_file, optimize=True, quality=95)
