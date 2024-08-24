
import json

class SaveGame:
    def __init__(self, game):
        self.game = game

    def save(self, data):
        with open('save_file.json', 'w') as save_file:
            json.dump(data, save_file)

    def load_last_game(self):
        try:
            with open('save_file.json', 'r') as save_file:
                data = json.load(save_file)
                # Load the saved state, for example:
                # self.game.load_room(Room1)
        except FileNotFoundError:
            print("No save file found. Starting a new game.")
            self.game.start_new_game()
