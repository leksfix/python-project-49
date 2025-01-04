import random

INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a    


def game_question():
    n1 = random.randrange(1, 100)
    n2 = random.randrange(1, 100)
    return (f'{n1} {n2}', str(gcd(n1, n2)))
