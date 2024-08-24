
import subprocess
import os

class RhubarbIntegration:
    def __init__(self, rhubarb_executable):
        self.rhubarb_executable = rhubarb_executable

    def generate_lip_sync_data(self, audio_file, output_json):
        command = [
            self.rhubarb_executable,
            audio_file,
            "-o", output_json
        ]
        subprocess.call(command)

    def batch_process(self, audio_directory, output_directory):
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        for filename in os.listdir(audio_directory):
            if filename.endswith(".opus"):
                audio_file = os.path.join(audio_directory, filename)
                output_json = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.json")
                self.generate_lip_sync_data(audio_file, output_json)

if __name__ == "__main__":
    rhubarb = RhubarbIntegration("path/to/rhubarb")
    rhubarb.batch_process("assets/audio/speech", "assets/lip_sync_data")
