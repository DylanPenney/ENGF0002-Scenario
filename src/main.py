import random

class Main:
	def __init__(self):
		while True:
			self.starter_question()
			# self.word_question()

	# Acts as a menu for questions (warm-up)
	def starter_question(self):

		data = self.get_starter_question()
		independent_event = (data[2] == "independent")

		# Regardless whether events are dependent or independent, P(A) and P(B) are calulated as such
		A = self.round_to_dp(random.uniform(0.1, 1.0), 2)
		B = self.round_to_dp(random.uniform(0.1, 1.0), 2)

		# P(A ∩ B) is only var to differ based on dependency
		if (independent_event):
			# for independent events only
			AandB = self.round_to_dp(A * B, 2)
			AorB = self.round_to_dp(A + B - AandB, 2)
		else:
			# dependent events
			AorB = -1
			while not AorB >= max(A, B): # Due to random element in P(A ∩ B) for dependent events
				AandB = self.round_to_dp(B * random.uniform(0.01, 1), 2) # P(A | B) = P(A ∩ B) / P(B) --> P(A ∩ B) = P(B) * P(A | B)
				AorB = self.round_to_dp(A + B - AandB, 2)
			
		question = data[0].replace("PA", str(A)).replace("PB", str(B)).replace("AorB", str(AorB)).replace("AandB", str(AandB)) # String formatting
		solution = self.round_to_dp(eval(data[1]), 2)
		
		self.check_solution(question, solution)

	# Acts as a menu for questions (word)
	def word_question(self):
		random_numbers = [random.randint(1, 10) for i in range(5)]
		pair = self.get_word_question()

		question = pair[0].replace("R1", str(random_numbers[0])).replace("R2", str(random_numbers[1]))
		solution = self.round_to_dp(eval(pair[1]), 2)
		self.check_solution(question, solution)

	# Provides interface with a random question and answer from the selection of warm up questions
	def get_starter_question(self):
		with open('../warm-up-questions/starter-questions/starter-questions.txt', 'r') as q:
			questions = q.readlines()
		with open('../warm-up-questions/starter-questions/starter-solutions.txt', 'r') as s:
			solutions = s.readlines()
		index = random.randint(0, min(len(questions), len(solutions) - 1))
		question = self.format_raw_question(questions[index])
		solution = self.format_raw_solution(solutions[index])
		if "independent" in question:
			return question, solution, "independent"
		else:
			return question, solution, "dependent"

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
		user_answer = self.round_to_dp(float(input(">>>")), 2)
		while user_answer != solution:
			user_answer = float(input("Incorrect!\n>>>"))
		print("Correct!")

	def round_to_dp(self, val, digits=2):
		precision = 10 ** digits
		return (round(precision * val) / precision)

Main()