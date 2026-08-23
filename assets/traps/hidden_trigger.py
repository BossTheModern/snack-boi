'''
    hidden_trigger.py

    handles logic for spawning hidden trigger on the parallel dimension
'''
from assets.spawnable.spawnable import Spawnable
from boards.board import Board

class HiddenTrigger(Spawnable):
    def __init__(self) -> None:
        super().__init__('T')

    def spawn(self, board: Board) -> None:
        super().spawn(board, hidden=True)