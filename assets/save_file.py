'''
    save_file.py

    Handles save file logic (load, save, delete) for files sent from
    save_files directory as argument upon initialization

    Target file format:
    highest_unlcoked_level: (int number)
    highest_cleared_level: (int number)
'''
import os
from typing import Dict, List
from assets.levels.level import Level
import keyboard
from keyboard import KeyboardEvent

class SaveFile:
    def __init__(self, file_path: str) -> None:
        self._file_path: str = file_path
        self._data: Dict[str, int] = {}
        self._already_saved: bool = False

    def load(self, levels: List[Level]) -> None:
        '''
            Loads specified file and its data to class, then unlocks and clears 
            levels accordingly
        '''
        highest_unlocked_lvl: int = 0
        highest_cleared_lvl: int = 0
        lvl_format_error: bool = False

        try:            
            with open(self._file_path) as file:
                highest_unlocked_lvl = int(file.readline().strip().split(':')[1])
                highest_cleared_lvl = int(file.readline().strip().split(':')[1])

                if highest_unlocked_lvl - highest_cleared_lvl != 1:
                    lvl_format_error = True
                    raise ValueError()

                self._data = {
                    'highest_unlocked_lvl': highest_unlocked_lvl,
                    'highest_cleared_lvl': highest_cleared_lvl
                }

                print("Save file loaded successfully")

            # Load levels state using number of levels unlocked and cleared
            for lvl_index in range(self._data['highest_unlocked_lvl']):
                if lvl_index < len(levels):
                    levels[lvl_index]._unlocked = True
                else: 
                    print(f"Warning: Level index {lvl_index} exceeds available levels. Skipping.")
            
            for lvl_index in range(self._data['highest_cleared_lvl']):
                if lvl_index < len(levels):
                    levels[lvl_index]._cleared = True
                else: 
                    print(f"Warning: Level index {lvl_index} exceeds available levels. Skipping.")

        except FileNotFoundError:
            print("File not found. Game will load without saved data")
        except ValueError:
            if lvl_format_error:
                print("Error, invalid data format: highest_unlocked_lvl must be one higher than highest_cleared_lvl") 
            else: 
                print("Error parsing data in file. Please check the file format.")
        except Exception as e:
            print(f"Error while loading save file: {e}")
    
    def save(self, levels: List[Level]) -> None:
        '''
            Saves game level progression to class and writes the new 
            progression to target file
        '''
        # Find the highest unlocked and cleared levels
        highest_unlocked_level: int = 0
        highest_cleared_level: int = 0
        index: int = 0
        
        # Fetch highest unlocked and cleared levels
        while True:
            if levels[index]._unlocked:
                highest_unlocked_level = index + 1
            if levels[index]._cleared:
                highest_cleared_level = index + 1
            index += 1

            if index >= len(levels) or (not levels[index]._unlocked and not levels[index]._cleared):
                break
        
        self._data['highest_unlocked_lvl'] = highest_unlocked_level
        self._data['highest_cleared_lvl'] = highest_cleared_level

        try:
            with open(self._file_path, 'w') as file:
                print("Saving data...")
                file.write(f"highest_unlocked_level: {self._data['highest_unlocked_lvl']}")
                file.write(f"\nhighest_cleared_level: {self._data['highest_cleared_lvl']}")
                
                print("Save file saved successfully")
                self._already_saved = True
        except FileNotFoundError:
            print("File not found. Cannot save data.")
        except Exception as e:
            print(f"Error while saving to file: {e}")       
        
    
    def delete(self) -> None:
        try:
            print("Deleting save file...")
            os.remove(self._file_path)
            print("Save file deleted successfully")
        except FileNotFoundError:
            print("File not found. Nothing to delete.")
        except Exception as e:
            print(f"Error while deleting file: {e}")
    
    def save_prompt(self, key_event: KeyboardEvent, levels: List[Level]) -> None:
            print("Do you want to save your progress? (y/n)")
            while True:
                key_event = keyboard.read_event(suppress=True)
                if key_event.event_type == keyboard.KEY_DOWN and key_event.name in ['y', 'n']:
                    break
            if key_event.name == 'y':
                print("Saving progress...")
                self.save(levels)
            elif key_event.name == 'n':
                print("Progress kept as it is")