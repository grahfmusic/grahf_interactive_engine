
import pyglet

class CreditsScreen:
    def __init__(self, window, game):
        self.window = window
        self.game = game

        self.background = pyglet.resource.image('assets/images/credits_background.png')
        self.label = pyglet.text.Label('Game Credits',
                                       font_name='Arial',
                                       font_size=48,
                                       x=window.width // 2, 
                                       y=window.height - 100,
                                       anchor_x='center', anchor_y='center')

        self.credits_text = pyglet.text.Label('Developed by: Your Name
Artwork: Artist Name
Music: Composer Name',
                                              font_name='Arial',
                                              font_size=24,
                                              x=window.width // 2,
                                              y=window.height // 2,
                                              anchor_x='center', anchor_y='center')

        self.window.push_handlers(self.on_draw, self.on_key_press)

    def on_draw(self):
        self.window.clear()
        self.background.blit(0, 0)
        self.label.draw()
        self.credits_text.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            self.game.show_menu()

    def cleanup(self):
        self.window.pop_handlers()
