import random

class Main:
	def __init__(self):
		self.warm_up_question()
		self.word_question()

	# Acts as a menu for questions (warm-up)
	def warm_up_question(self):
		A = round(random.uniform(0.1, 1.0), 2)
		B = round(random.uniform(0.1, 1.0), 2)
		AorB = round(A + B, 2)
		AandB = round(A * B, 2)
		AgivenB = round(AandB / B, 2)
		pair = self.get_warm_up_question()

		question = pair[0].replace("PA", str(A)).replace("PB", str(B)).replace("AorB", str(AorB)).replace("AandB", str(AandB)).replace("AgivenB", str(AgivenB))
		solution = round(eval(pair[1]), 2)
		self.check_solution(question, solution)

	# Acts as a menu for questions (word)
	def word_question(self):
		random_numbers = [random.randint(1, 10) for i in range(5)]
		pair = self.get_word_question()

		question = pair[0].replace("R1", str(random_numbers[0])).replace("R2", str(random_numbers[1]))
		solution = round(eval(pair[1]), 2)
		self.check_solution(question, solution)

	# Provides interface with a random question and answer from the selection of warm up questions
	def get_warm_up_question(self):
		with open('../warm-up-questions/warm-up-questions.txt', 'r') as q:
			questions = q.readlines()
		with open('../warm-up-questions/warm-up-solutions.txt', 'r') as s:
			solutions = s.readlines()
		index = random.randint(0, min(len(questions), len(solutions) - 1))
		question = self.format_raw_question(questions[index])
		solution = self.format_raw_solution(solutions[index])
		return question, solution

	def get_word_question(self):
		with open('../word-questions/questions.txt') as q:
			questions = q.readlines()
		with open('../word-questions/solutions.txt') as s:
			solutions = s.readlines()
		index = random.randint(0, min(len(questions), len(solutions) - 1))
		question = self.format_raw_question(questions[index])
		solution = self.format_raw_solution(solutions[index])
		return question, solution

	def format_raw_question(self, line):
		line = str(line).encode().decode('utf-8').replace('\n', '')
		return line
	def format_raw_solution(self, line):
		line = str(line).encode().decode('utf-8').replace('\n', '')
		return line

	def check_solution(self, question, solution):
		user_answer = -1 # Turn while loop into a 'do-while' loop
		print(question)
		print("Answer to two decimal places (where applicable).")
		user_answer = round(float(input(">>>")), 2)
		while user_answer != solution:
			user_answer = float(input("Incorrect!\n>>>"))
		print("Correct!")

Main()