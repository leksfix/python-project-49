import random

INSTRUCTION = 'What is the result of the expression?'


def calculate(a, b, op):
    match op:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b


def game_question():
    n1 = random.randrange(1, 100)
    n2 = random.randrange(1, 100)
    operation = random.choice(['+', '-', '*'])
    return (f'{n1} {operation} {n2}', str(calculate(n1, n2, operation)))
