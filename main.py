import random

class Main:
	def __init__(self):
		pass

	# Provides interface with a random question from the selection of warm up questions
	def get_warm_up_question(self):
		with open('warm-up-questions.txt') as f:
			lines = f.readlines()
			return self.format_raw_question(random.choice(lines))

	def get_word_question(self):
		with open('questions.txt') as f:
			lines = f.readlines()		
			return self.format_raw_question(random.choice(lines))

	def format_raw_question(self, line):
		line = str(line).encode().decode('unicode-escape') #.replace("|", "\n")
		return line

Main()