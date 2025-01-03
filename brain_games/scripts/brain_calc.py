# from brain_games.even import run
from brain_games.game import run_game
from brain_games.calc import INSTRUCTION, game_question


def main():
	run_game(INSTRUCTION, game_question)


if __name__ == "__main__":
    main()
