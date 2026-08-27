'''
    test_save_file.py

    tests for save_file.py
'''

import unittest
from unittest.mock import patch
import os
import sys
import copy

current_dir: str = os.path.dirname(os.path.abspath(__file__))
parent_dir: str = os.path.dirname(current_dir)
root_dir: str = os.path.dirname(parent_dir)
sys.path.insert(0, root_dir)

from assets.save_file import SaveFile
from assets.levels.levels import Levels
from assets.levels.level import Level
from account.account import Account
from typing import List
from io import StringIO

class TestSaveFile(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_load_save_file(self, mock_stdout) -> None:
        '''
            Testing if loading a normal save file works as intended
        '''
        account: Account = Account()
        save_file: SaveFile = SaveFile("tests/savefile/save_file_tests/test_save_normal.txt", account)
        levels: List[Level] = copy.deepcopy(Levels._levels)
        save_file.load(levels)
        output: StringIO = mock_stdout.getvalue()

        self.assertTrue(levels[4]._unlocked)
        self.assertTrue(levels[3]._cleared)
        self.assertIn("Save file loaded successfully", output)      

    @patch('sys.stdout', new_callable=StringIO)
    def test_load_save_file_invalid_format(self, mock_stdout) -> None:
        '''
            Testing if loading a save file with invalid format is handled
            correctly
        '''
        account: Account = Account()
        save_file: SaveFile = SaveFile("tests/savefile/save_file_tests/test_save_invalid_format.txt", account)
        levels: List[Level] = copy.deepcopy(Levels._levels)
        save_file.load(levels)
        output: StringIO = mock_stdout.getvalue()

        self.assertFalse(levels[3]._unlocked)
        self.assertFalse(levels[2]._cleared)
        self.assertIn("Error, invalid data format: highest_unlocked_lvl must be one higher than highest_cleared_lvl", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_load_save_file_nonexistent(self, mock_stdout) -> None:
        '''
            Testing if a nonexistant save file is handled accordingly
        '''
        account: Account = Account()
        save_file: SaveFile = SaveFile("tests/savefile/save_files/nonexistant.txt", account)
        levels: List[Level] = copy.deepcopy(Levels._levels)
        save_file.load(levels)
        output: StringIO = mock_stdout.getvalue()

        self.assertFalse(levels[3]._unlocked)
        self.assertFalse(levels[2]._cleared)
        self.assertIn("File not found. Game will load without saved data", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_save_file(self, mock_stdout) -> None:
        '''
            Tests if save file saves correctly
        '''
        
        expected_highest_unlocked: int = 5
        expected_highest_cleared: int = 4

        account: Account = Account()
        save_file: SaveFile = SaveFile("tests/savefile/save_file_tests/test_new_save.txt", account)
        levels: List[Level] = copy.deepcopy(Levels._levels)
        for i in range(expected_highest_unlocked):
            levels[i]._unlocked = True
        for i in range(expected_highest_cleared):
            levels[i]._cleared = True
        
        save_file.save(levels)
        output: StringIO = mock_stdout.getvalue()

        self.assertEqual(expected_highest_unlocked, save_file._data['highest_unlocked_lvl'])
        self.assertEqual(expected_highest_cleared, save_file._data['highest_cleared_lvl'])
        self.assertEqual(save_file._data['highest_unlocked_lvl'] - save_file._data['highest_cleared_lvl'], 1)
        self.assertIn("Save file saved successfully", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_delete_file(self, mock_stdout) -> None:
        '''
            Tests if save file deletes correctly
        '''
        account: Account = Account()
        save_file: SaveFile = SaveFile("tests/savefile/save_file_tests/test_deleted_save.txt", account)
        levels: List[Level] = copy.deepcopy(Levels._levels)
        output: StringIO

        save_file.save(levels)
        save_file.delete()
        output = mock_stdout.getvalue()

        self.assertFalse(os.path.exists(save_file._file_path))
        self.assertIn("Save file deleted successfully", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_delete_nonexistent_file(self, mock_stdout) -> None:
        '''
            Tests if deleting a nonexistent file is handled correctly    
        '''
        account: Account = Account()
        save_file: SaveFile = SaveFile("tests/savefile/save_file_tests/test_nonexistent_delete_file.txt", account)
        save_file.delete()
        output: StringIO = mock_stdout.getvalue()

        self.assertIn("File not found. Nothing to delete.", output)


if __name__ == "__main__":
    unittest.main()