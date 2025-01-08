"""
Brain games welcome module
"""
import prompt


def welcome_user():
	"""
	Prompts for username and prints welcome message
	"""
	print('Welcome to the Brain Games!')
	username = prompt.string('May I have your name? ')
	print(f'Hello, {username}!')

