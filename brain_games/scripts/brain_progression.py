"""Launch script for brain-progression game"""
import brain_games.games.progression as progression
from brain_games.game import run_game


def main():
    """Runs the game with questions from the 'progression' module"""
    run_game(progression)


if __name__ == "__main__":
    main()
