import json
import subprocess
import sys
import shlex
import logging

class CommandConverter:
    def __init__(self, command_mappings_file, arg_mappings_file):
        with open(command_mappings_file, 'r') as file:
            self.command_map = json.load(file)
        with open(arg_mappings_file, 'r') as file:
            self.arg_map = json.load(file)
        logging.basicConfig(level=logging.INFO)

    def translate_args(self, args):
        translated_args = []
        for arg in args:
            translated_arg = self.arg_map.get(arg, arg)  # Default to original arg if no translation found
            translated_args.append(translated_arg)
        return translated_args

    def convert(self, ubuntu_command):
        ubuntu_command_parts = shlex.split(ubuntu_command)
        manjaro_command_base = self.command_map.get(ubuntu_command_parts[1])
        if manjaro_command_base:
            translated_args = self.translate_args(ubuntu_command_parts[2:])
            dynamic_parts = " ".join(translated_args)
            return f"{manjaro_command_base} {dynamic_parts}"
        else:
            logging.warning(f'No direct match for {ubuntu_command_parts[1]}')
            return None

    def execute(self, manjaro_command):
        logging.info(f'Executing: {manjaro_command}')
        subprocess.run(manjaro_command, shell=True)

if __name__ == "__main__":
    ubuntu_command = ' '.join(sys.argv[1:])
    converter = CommandConverter('mappings.json', 'arg_mappings.json')
    manjaro_command = converter.convert(ubuntu_command)
    if manjaro_command:
        converter.execute(manjaro_command)
    else:
        logging.error(f'Failed to convert: {ubuntu_command}')
