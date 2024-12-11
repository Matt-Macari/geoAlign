###################################################################################
# Developed by Matthew Marcotullio, Matt Macari, Lily Yassemi, and Dylan Lucas    #
#             for California Polytechnic State University, Humboldt               #
###################################################################################
import os
import unittest
from unittest.mock import patch
from src.path_prompt import get_input_path, get_output_path

class TestPathPrompt(unittest.TestCase):

    @patch('src.path_prompt.input')
    @patch('src.path_prompt.os')
    def test_get_input_path_exit(self, mock_os, mock_input):
        mock_input.side_effect = ['exit']
        result = get_input_path()
        self.assertEqual(result, ("exit", 0))

    @patch('src.path_prompt.input')
    @patch('src.path_prompt.os.listdir')
    @patch('src.path_prompt.os.path.isdir')
    @patch('src.path_prompt.os.path.isfile')
    @patch('src.path_prompt.os.path.getsize')
    def test_get_input_path_valid_tif_files(self, mock_getsize, mock_isfile, mock_isdir, mock_listdir, mock_input):
        # Mock test directory and files
        test_dir = 'unit/valid_folder'

        # Ensure the directory exists (create if not)
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)

        # Create test files
        test_files = ['file1.tif', 'file2.tif', 'file3.txt']
        for file in test_files:
            with open(os.path.join(test_dir, file), 'w') as f:
                f.write('dummy content')

        # Mock inputs and file system behaviors
        mock_input.return_value = test_dir
        mock_isdir.return_value = True
        mock_listdir.return_value = test_files
        mock_isfile.side_effect = lambda path: os.path.basename(path) in test_files
        mock_getsize.side_effect = [5000000, 1500000, 0]  # Sizes for files

        # Call the function
        result, num_tif_files = get_input_path()

        # Assertions
        self.assertEqual(result, test_dir)
        self.assertEqual(num_tif_files, 2)

        # Cleanup
        for file in test_files:
            os.remove(os.path.join(test_dir, file))
        os.rmdir(test_dir)

    @patch('src.path_prompt.input')
    @patch('src.path_prompt.os')
    def test_get_output_path_exit(self, mock_os, mock_input):
        mock_input.side_effect = ['exit']
        result = get_output_path()
        self.assertEqual(result, "exit")

    @patch('src.path_prompt.input')
    @patch('src.path_prompt.os.path.isdir')
    def test_get_output_path_valid_directory(self, mock_isdir, mock_input):
        
        mock_input.return_value = 'mock/output_folder'
        mock_isdir.return_value = True

        result = get_output_path()

        self.assertEqual(result, 'mock/output_folder')

if __name__ == '__main__':
    unittest.main()
