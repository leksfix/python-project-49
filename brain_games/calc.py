
import random

INSTRUCTION = 'What is the result of the expression?'

def game_question():
    n1 = random.randrange(1, 100)
    n2 = random.randrange(1, 100)
    match random.randrange(1, 4):
        case 1:
            question = f'{n1} + {n2}'
            answer = n1 + n2
        case 2:
            question = f'{n1} - {n2}'
            answer = n1 - n2
        case _:
            question = f'{n1} * {n2}'
            answer = n1 * n2
    return (question, str(answer))


