import random

INSTRUCTION = 'What number is missing in the progression?'

progression_length = None


def game_question():
    global progression_length
    if progression_length is None:
        progression_length = random.randrange(5, 11)
    hidden_pos = random.randrange(0, progression_length)
    step = random.randrange(1, 10)
    n = random.randrange(1, 100)
    question = ''
    for i in range(progression_length):
        if i == hidden_pos:
            question = question + ' ..'
            hidden = str(n)
        else:
            question = question + ' ' + str(n)
        n += step
    return (question.lstrip(), hidden)
