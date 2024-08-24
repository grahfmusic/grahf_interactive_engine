
import pyglet
from menu_screen import MenuScreen
from room1 import Room1
from room2 import Room2
from settings import SettingsScreen
from credits import CreditsScreen
from save_game import SaveGame
from fmod_manager import FMODManager

class Game:
    def __init__(self):
        self.window = pyglet.window.Window(width=800, height=600)
        self.current_screen = None
        self.fmod_manager = FMODManager()

        self.show_menu()

    def show_menu(self):
        if self.current_screen:
            self.current_screen.cleanup()
        self.current_screen = MenuScreen(self.window, self)

    def start_new_game(self):
        if self.current_screen:
            self.current_screen.cleanup()
        self.load_room(Room1)

    def load_game(self):
        if self.current_screen:
            self.current_screen.cleanup()
        save_game = SaveGame(self)
        save_game.load_last_game()

    def show_settings(self):
        if self.current_screen:
            self.current_screen.cleanup()
        self.current_screen = SettingsScreen(self.window, self)

    def show_credits(self):
        if self.current_screen:
            self.current_screen.cleanup()
        self.current_screen = CreditsScreen(self.window, self)

    def load_room(self, room_class):
        if self.current_screen:
            self.current_screen.cleanup()
        self.current_screen = room_class(self.window)

    def run(self):
        pyglet.app.run()

if __name__ == "__main__":
    game = Game()
    game.run()
