'''
    test_save_file.py

    tests for save_file.py
'''

import unittest
from save_file import SaveFile
from assets.levels.levels import Levels
from assets.levels.level import Level
from typing import List

class TestSaveFIle(unittest.TestCase):
    def test_load_save_file(self):
        save_file: SaveFile = SaveFile("tests/savefile/test_save1.txt")
        levels: List[Level] = Levels._classic_levels_set_1.copy()
        save_file.load(levels)
        self.assertTrue(levels[0]._unlocked)      

    def test_load_save_file_invalid_format(self):
        pass

    def test_load_save_file_nonexistent(self):
        pass

    def test_save_file(self):
        pass
        

if __name__ == "__main__":
    unittest.main()