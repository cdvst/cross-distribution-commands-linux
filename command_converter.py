import json
import subprocess
import sys

class CommandConverter:
    def __init__(self, mapping_file):
        with open(mapping_file, 'r') as file:
            self.command_mappings = json.load(file)

    def convert_command(self, command):
        ubuntu_command = command.split()
        if ubuntu_command[0] in self.command_mappings:
            manjaro_command = self.command_mappings[ubuntu_command[0]]
            manjaro_command.extend(ubuntu_command[1:])
            return ' '.join(manjaro_command)
        else:
            print(f"Command {ubuntu_command[0]} not found in mappings.")
            sys.exit(1)

    def execute_command(self, command):
        try:
            process = subprocess.Popen(command, shell=True)
            process.communicate()
        except Exception as e:
            print(f"Failed to execute command: {e}")
            sys.exit(1)

if __name__ == "__main__":
    converter = CommandConverter('command_mappings.json')
    if len(sys.argv) > 1:
        ubuntu_command = sys.argv[1]
        manjaro_command = converter.convert_command(ubuntu_command)
        converter.execute_command(manjaro_command)
    else:
        print("No command provided.")
        sys.exit(1)
