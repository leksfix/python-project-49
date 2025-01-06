import prompt

ROUNDS_COUNT = 3


def run_game(game_module):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print(game_module.INSTRUCTION)
    correct_answers_count = 0
    while correct_answers_count < ROUNDS_COUNT:        
        question, correct_answer = game_module.game_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            return
        correct_answers_count += 1
    print(f'Congratulations, {username}!')
