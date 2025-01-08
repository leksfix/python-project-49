"""Launch script for brain-even game"""
import brain_games.games.even as even
from brain_games.game import run_game


def main():
    """Runs the game with questions from the 'even' module"""
    run_game(even)


if __name__ == "__main__":
    main()
