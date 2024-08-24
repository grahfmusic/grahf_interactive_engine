
import json
import os

class DialogueManager:
    def __init__(self, room_name):
        self.room_name = room_name
        self.dialogue = {}

    def add_dialogue(self, char_name, interaction, lines):
        if interaction not in self.dialogue:
            self.dialogue[interaction] = {}
        self.dialogue[interaction][char_name] = lines

    def generate_filenames(self):
        filenames = []
        for interaction, lines in self.dialogue.items():
            for char_name, char_lines in lines.items():
                for i, line in enumerate(char_lines, start=1):
                    filename = f"{char_name}-{self.room_name}-{interaction}-{i}.opus"
                    filenames.append(filename)
        return filenames

    def export_dialogue_json(self, output_file):
        with open(output_file, 'w') as f:
            json.dump(self.dialogue, f, indent=4)

    def generate_filenames_json(self, output_file):
        filenames = self.generate_filenames()
        with open(output_file, 'w') as f:
            json.dump(filenames, f, indent=4)

if __name__ == "__main__":
    manager = DialogueManager("room1")
    manager.add_dialogue("hero", "greeting", ["Hello!", "How are you?"])
    manager.add_dialogue("villain", "threat", ["You will not survive!", "Prepare to meet your doom!"])
    
    manager.export_dialogue_json("dialogue_files/room1_dialogue.json")
    manager.generate_filenames_json("dialogue_files/room1_filenames.json")
