"""
Questions/answers for brain-calc game
"""
import random

INSTRUCTION = 'What number is missing in the progression?'

PROGRESSION_LENGTH = 10


def get_progression():
    """
    Generates progression with random values
    """
    n = random.randrange(1, 100)
    step = random.randrange(1, 10)
    res = []
    for i in range(PROGRESSION_LENGTH):
        res.append(str(n))
        n += step
    return res


def game_question():
    """
    Returns question and correct answer
    """
    prg = get_progression()
    hidden_pos = random.randrange(0, PROGRESSION_LENGTH)
    hidden = prg[hidden_pos]
    prg[hidden_pos] = '..'
    return (' '.join(prg), hidden)
