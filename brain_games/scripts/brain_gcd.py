"""Launch script for brain-gcd game"""
import brain_games.games.gcd as gcd
from brain_games.game import run_game


def main():
    """Runs the game with questions from the 'gcd' module"""
    run_game(gcd)


if __name__ == "__main__":
    main()
