import unittest
from unittest.mock import patch, MagicMock
import os
from src.folder_prompt import select_input_folder, select_output_folder
from tkinter import filedialog

class TestFolderSelection(unittest.TestCase):

    @patch('tkinter.filedialog.askdirectory')
    def test_select_directory(mock_askdirectory):
        mock_askdirectory.return_value = 'unit/test_empty_path'
        result = select_input_folder()
        assert result == 'unit/test_empty_path'

if __name__ == '__main__':
    unittest.main()
