import prompt
import random


def run():
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers_count = 0
    while correct_answers_count < 3:
        n = random.randrange(1, 100)
        print(f'Question: {n}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = 'no' if n % 2 else 'yes'
        if user_answer == correct_answer:
            correct_answers_count += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return
    print(f'Congratulations, {username}!')