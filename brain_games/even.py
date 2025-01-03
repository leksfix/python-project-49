
import random

INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def game_question():
    n = random.randrange(1, 100)
    return (str(n), 'no' if n % 2 else 'yes')


