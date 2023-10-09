import unittest
from command_converter import CommandConverter

class TestCommandConverter(unittest.TestCase):

    def setUp(self):
        self.converter = CommandConverter('mappings.json')

    def test_update_command(self):
        ubuntu_command = 'apt update'
        expected_manjaro_command = 'sudo pacman -Sy'
        self.assertEqual(self.converter.convert(ubuntu_command), expected_manjaro_command)

    def test_upgrade_command(self):
        ubuntu_command = 'apt upgrade'
        expected_manjaro_command = 'sudo pacman -Su'
        self.assertEqual(self.converter.convert(ubuntu_command), expected_manjaro_command)

    def test_install_command(self):
        ubuntu_command = 'apt install package_name'
        expected_manjaro_command = 'sudo pacman -S package_name'
        self.assertEqual(self.converter.convert(ubuntu_command), expected_manjaro_command)

    def test_remove_command(self):
        ubuntu_command = 'apt remove package_name'
        expected_manjaro_command = 'sudo pacman -R package_name'
        self.assertEqual(self.converter.convert(ubuntu_command), expected_manjaro_command)

    # Additional tests for edge cases and other command variations
    def test_non_existent_command(self):
        ubuntu_command = 'apt non_existent_command'
        self.assertIsNone(self.converter.convert(ubuntu_command))

if __name__ == '__main__':
    unittest.main()
