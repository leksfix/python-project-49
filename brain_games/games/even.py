import random

INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(n):
    return not n % 2


def game_question():
    n = random.randrange(1, 100)
    return (str(n), 'yes' if is_even(n) else 'no')
