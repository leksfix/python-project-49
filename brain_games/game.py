import prompt



CORRECT_GOAL = 3


def run_game(instruction, game_question):

    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print(instruction)
    correct_answers_count = 0
    while correct_answers_count < CORRECT_GOAL:
        question, correct_answer = game_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            correct_answers_count += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return
    print(f'Congratulations, {username}!')
