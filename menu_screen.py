
import pyglet

class MenuScreen:
    def __init__(self, window, game):
        self.window = window
        self.game = game
        self.options = ["New Game", "Load Game", "Settings", "Credits", "Quit Game"]
        self.selected_index = 0

        self.background = pyglet.resource.image('assets/images/menu_background.png')
        self.labels = self.setup_labels()

        self.window.push_handlers(self.on_draw, self.on_key_press)

    def setup_labels(self):
        labels = []
        for i, option in enumerate(self.options):
            label = pyglet.text.Label(option,
                                      font_name='Arial',
                                      font_size=36,
                                      x=self.window.width // 2, 
                                      y=self.window.height // 2 - i * 60,
                                      anchor_x='center', anchor_y='center')
            labels.append(label)
        return labels

    def on_draw(self):
        self.window.clear()
        self.background.blit(0, 0)
        for i, label in enumerate(self.labels):
            label.color = (255, 255, 0, 255) if i == self.selected_index else (255, 255, 255, 255)
            label.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.UP:
            self.selected_index = (self.selected_index - 1) % len(self.options)
        elif symbol == pyglet.window.key.DOWN:
            self.selected_index = (self.selected_index + 1) % len(self.options)
        elif symbol == pyglet.window.key.ENTER:
            self.select_option()

    def select_option(self):
        option = self.options[self.selected_index]
        if option == "New Game":
            self.game.start_new_game()
        elif option == "Load Game":
            self.game.load_game()
        elif option == "Settings":
            self.game.show_settings()
        elif option == "Credits":
            self.game.show_credits()
        elif option == "Quit Game":
            pyglet.app.exit()

    def cleanup(self):
        self.window.pop_handlers()
