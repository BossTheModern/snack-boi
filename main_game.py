'''
    main_game.py

    the starting point of the game
'''
from game.snack_boi import Game

if __name__ == "__main__":
    game: Game = Game()
    game.game_menu()

    print("Quitting game, thanks for playing!")