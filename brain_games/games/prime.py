"""
Questions/answers for brain-prime game
"""
import math
import random

INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    """
    Checks if n is a prime number
    """
    if n <= 3:
        return n > 1
    i = 2
    while i <= math.sqrt(n):
        if not n % i:
            return False
        i += 1
    return True


def game_question():
    """
    Returns question and correct answer
    """
    n = random.randrange(2, 100)
    return (str(n), 'yes' if is_prime(n) else 'no')
