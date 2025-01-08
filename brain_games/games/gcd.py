"""
Questions/answers for brain-gcd game
"""
import random

INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    """
    Calculates greatest common divisor for a and b
    """
    while b != 0:
        a, b = b, a % b
    return a    


def game_question():
    """
    Returns question and correct answer
    """
    n1 = random.randrange(1, 100)
    n2 = random.randrange(1, 100)
    return (f'{n1} {n2}', str(gcd(n1, n2)))
