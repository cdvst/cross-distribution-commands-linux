#!/bin/bash

# Define the function and alias
echo 'function convert_and_execute() {
    translated_command=$(python ~/command_converter/CommandConverter.py "$1")
    if [[ $? -eq 0 ]]; then
        eval $translated_command
    else
        echo "Command translation failed."
    fi
}' >> ~/.bashrc

echo 'alias ubuntu="convert_and_execute"' >> ~/.bashrc

# Source the .bashrc file to load the function and alias
source ~/.bashrc

# Notify the user
echo "Setup complete. You can now use the 'ubuntu' alias to run Ubuntu commands."
