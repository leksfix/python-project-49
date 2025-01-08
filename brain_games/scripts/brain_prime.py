"""Launch script for brain-prime game"""
import brain_games.games.prime as prime
from brain_games.game import run_game


def main():
    """Runs the game with questions from the 'prime' module"""
    run_game(prime)


if __name__ == "__main__":
    main()
