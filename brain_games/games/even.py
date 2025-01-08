"""
Questions/answers for brain-even game
"""
import random

INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(n):
    """
    Checks if n is an even number
    """
    return not n % 2


def game_question():
    """
    Returns question and correct answer
    """
    n = random.randrange(1, 100)
    return (str(n), 'yes' if is_even(n) else 'no')
