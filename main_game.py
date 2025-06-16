# Starting point of the game
import os
import sys

current_dir: str = os.path.dirname(os.path.abspath(__file__))
game_dir: str = os.path.join(current_dir, 'game')

sys.path.insert(0, game_dir)

from snack_boi import Game

if __name__ == "__main__":
    game: Game = Game()
    game.game_menu()

    print("Quitting game, thanks for playing!")