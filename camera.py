
import pyglet

class Camera:
    def __init__(self, window):
        self.window = window
        self.view_x = 0
        self.view_y = 0
        self.scale_x = 1
        self.scale_y = 1
        self.update_viewport()

    def update_viewport(self):
        aspect_ratio = self.window.width / self.window.height
        
        if aspect_ratio >= 21/9:
            self.scale_x = aspect_ratio / (21/9)
            self.scale_y = 1
        elif aspect_ratio >= 16/9:
            self.scale_x = 1
            self.scale_y = 1
        else:
            self.scale_x = 16/9 / aspect_ratio
            self.scale_y = 1

        self.window.projection = pyglet.window.Projection2D()

    def begin(self):
        pyglet.gl.glPushMatrix()
        pyglet.gl.glScalef(self.scale_x, self.scale_y, 1)
        pyglet.gl.glTranslatef(-self.view_x, -self.view_y, 0)

    def end(self):
        pyglet.gl.glPopMatrix()

    def set_position(self, x, y):
        self.view_x = x
        self.view_y = y

    def resize(self, width, height):
        self.window.set_size(width, height)
        self.update_viewport()
