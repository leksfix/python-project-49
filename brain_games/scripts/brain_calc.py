"""Launch script for brain-calc game"""
import brain_games.games.calc as calc
from brain_games.game import run_game


def main():
    """Runs the game with questions from the 'calc' module"""
    run_game(calc)


if __name__ == "__main__":
    main()
