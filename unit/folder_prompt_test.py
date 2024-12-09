import unittest
from unittest.mock import patch
import os
from src.folder_prompt import select_input_folder, select_output_folder

class TestFolderPrompt(unittest.TestCase):

    @patch('src.folder_prompt.askdirectory')
    @patch('os.listdir')
    @patch('os.path.getsize')
    def test_select_input_folder_with_tiff_files(self, mock_getsize, mock_listdir, mock_askdirectory):
        # Set up a temporary directory for testing
        test_dir = 'unit/test_img'

        # Ensure the directory exists (create if not)
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)

        # Add some test files to the directory
        test_files = ['file1.tif', 'file2.tif', 'file3.txt']
        for file in test_files:
            with open(os.path.join(test_dir, file), 'w') as f:
                f.write('dummy content')

        # Simulate user selecting the test directory
        mock_askdirectory.return_value = test_dir

        # Simulate folder contents (mocking os.listdir for the test directory)
        mock_listdir.return_value = test_files 

        # Simulate file sizes for each file in the mocked directory
        mock_getsize.side_effect = [5000000, 1500000, 0]

        result, num_tif_files = select_input_folder()
        self.assertEqual(result, os.path.relpath(test_dir))
        self.assertEqual(num_tif_files, 2)

        # Remove the created files and folder
        for file in test_files:
            os.remove(os.path.join(test_dir, file))
        os.rmdir(test_dir)

    @patch('src.folder_prompt.askdirectory')
    def test_select_input_folder_cancel_selection(self, mock_askdirectory):
        # Simulate user canceling the selection
        mock_askdirectory.return_value = ''

        result, num_tif_files = select_input_folder()
        self.assertEqual(result, "exit")
        self.assertEqual(num_tif_files, 0)

    @patch('src.folder_prompt.askdirectory')
    def test_select_output_folder(self, mock_askdirectory):
        # Simulate user selecting a directory
        mock_askdirectory.return_value = '/mock/output_folder'

        result = select_output_folder()
        self.assertEqual(result, '/mock/output_folder')

    @patch('src.folder_prompt.askdirectory')
    def test_select_output_folder_cancel_selection(self, mock_askdirectory):
        # Simulate user canceling the selection
        mock_askdirectory.return_value = ''

        result = select_output_folder()
        self.assertEqual(result, "exit")


if __name__ == '__main__':
    unittest.main()