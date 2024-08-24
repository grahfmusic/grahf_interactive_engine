
import pyglet

class ShaderManager:
    def __init__(self):
        self.shaders = {}

    def load_shader(self, name, vertex_path, fragment_path):
        with open(vertex_path, 'r') as f:
            vertex_src = f.read()
        with open(fragment_path, 'r') as f:
            fragment_src = f.read()

        self.shaders[name] = pyglet.graphics.shader.ShaderProgram(
            pyglet.graphics.shader.Shader(vertex_src, 'vertex'),
            pyglet.graphics.shader.Shader(fragment_src, 'fragment')
        )

    def use_shader(self, name):
        if name in self.shaders:
            self.shaders[name].use()

    def stop_shader(self):
        pyglet.graphics.shader.ShaderProgram.stop()
