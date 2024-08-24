
import pyglet

class SettingsScreen:
    def __init__(self, window, game):
        self.window = window
        self.game = game
        self.options = ["Resolution", "Volume", "Display Mode", "Back"]
        self.selected_index = 0

        self.resolutions = [(800, 600), (1024, 768), (1280, 720), (1920, 1080), (2560, 1080), (3440, 1440)]
        self.selected_resolution = 0

        self.music_volume = 0.5
        self.sfx_volume = 0.5
        self.speech_volume = 0.5

        self.display_modes = ["Windowed", "Borderless", "Fullscreen"]
        self.selected_display_mode = 0

        self.background = pyglet.resource.image('assets/images/settings_background.png')
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
        if option == "Resolution":
            self.cycle_resolution()
        elif option == "Volume":
            self.adjust_volume()
        elif option == "Display Mode":
            self.cycle_display_mode()
        elif option == "Back":
            self.game.show_menu()

    def cycle_resolution(self, direction=1):
        self.selected_resolution = (self.selected_resolution + direction) % len(self.resolutions)
        self.apply_resolution()

    def adjust_volume(self, direction=1):
        if self.selected_option == 1:
            self.music_volume = min(max(self.music_volume + direction * 0.1, 0), 1)
            self.sfx_volume = min(max(self.sfx_volume + direction * 0.1, 0), 1)
            self.speech_volume = min(max(self.speech_volume + direction * 0.1, 0), 1)
            self.apply_volume_changes()

        elif self.selected_option == 3:
            self.selected_display_mode = (self.selected_display_mode + direction) % len(self.display_modes)
            self.apply_display_mode()

    def apply_resolution(self):
        width, height = self.resolutions[self.selected_resolution]
        self.window.set_size(width, height)
        self.game.current_screen.camera.resize(width, height)

    def apply_volume_changes(self):
        self.game.mixer.set_music_volume(self.music_volume)
        self.game.mixer.set_sfx_volume(self.sfx_volume)
        self.game.mixer.set_speech_volume(self.speech_volume)

    def apply_display_mode(self):
        mode = self.display_modes[self.selected_display_mode]
        if mode == "Windowed":
            self.window.set_fullscreen(False)
        elif mode == "Borderless":
            self.window.set_fullscreen(False, windowed=False)
        elif mode == "Fullscreen":
            self.window.set_fullscreen(True)

    def cleanup(self):
        self.window.pop_handlers()
