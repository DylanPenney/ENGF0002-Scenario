import random

class Main:
	def __init__(self):
		pass

	# Provides interface with a random question and answer from the selection of warm up questions
	def get_warm_up_question(self):
		with open('warm-up-questions.txt') as q:
			questions = q.readlines()
		with open('warm-up-solutions.txt') as s:
			solutions = s.readlines()
		index = random.randint(0, min(len(questions), len(solutions) - 1))
		question = self.format_raw_question(questions[index])
		solution = self.format_raw_solution(solutions[index])
		return question, solution

	def get_word_question(self):
		with open('questions.txt') as f:
			lines = f.readlines()		
			return self.format_raw_question(random.choice(lines))

	def format_raw_question(self, line):
		line = str(line)[:-1].encode().decode('utf-8')[:-1]
		return line
	def format_raw_solution(self, line):
		line = str(line).encode().decode('utf-8')[:-1]
		return line

Main()