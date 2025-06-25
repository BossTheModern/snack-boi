'''
    debug.py

    module containing debug related methods
'''
from typing import List
import os
import sys

current_dir: str = os.path.dirname(os.path.abspath(__file__))
parent_dir: str = os.path.dirname(current_dir)
assets_dir: str = os.path.join(parent_dir, 'assets')
snacks_dir: str = os.path.join(assets_dir, 'snacks')
traps_dir: str = os.path.join(assets_dir, 'traps')
powerups_dir: str = os.path.join(assets_dir, 'powerups')

sys.path.insert(0, snacks_dir)
sys.path.insert(0, traps_dir)
sys.path.insert(0, powerups_dir)

from snack import Snack
from traps import Trap
from recon_snack import ReconSnack


def print_obj_tracker(occupied_positions: List[List[int]], snack: Snack, traps: List[Trap], recon_snack: ReconSnack) -> None:
        '''
            Tracks all objects existing in the board by providing positional
            data for each of them. Used for debugging purposes
        '''
        print(f"Current snack position: {snack._position}")
        print(f"Number of traps: {len(traps)}")
        
        print(f"Trap positions: {[trap._position for trap in traps]}")
        print(f"Hunger traps: {len([trap for trap in traps if trap._type == 'hunger'])}")
        print(f"Hunger traps positions: {[trap._position for trap in traps if trap._type == 'hunger']}")
        print(f"Parallel traps: {len([trap for trap in traps if trap._type == 'parallel dimension'])}")
        print(f"Parallel traps positions: {[trap._position for trap in traps if trap._type == 'parallel dimension']}")
        print(f"Recon snack position: {recon_snack._position}")
        print(f"Overall occupied positions: {occupied_positions}")

        if snack._position in [trap._position for trap in traps]:
            print("Snack in same position as trap")
        
        if snack._position == recon_snack._position:
            print("Snack in same position as recon snack")

        if recon_snack._position in [trap._position for trap in traps]:
            print("Recon snack in same position as trap")