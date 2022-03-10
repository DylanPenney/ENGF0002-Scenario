class Main:
	def __init__(self):
		self.get_word_question()
		self.get_warm_up_question()

	def get_warm_up_question(self):
		with open('warm-up-questions.txt') as f:
			lines = f.readlines()
			for i in range(0, len(lines)): # doesn't work when using enhanced for??
				lines[i] = self.format_raw_question(lines[i])
				print(lines[i])

	def get_word_question(self):
		with open('questions.txt') as f:
			lines = f.readlines()
			for i in range(0, len(lines)):
				lines[i] = self.format_raw_question(lines[i])
				print(lines[i])

	def format_raw_question(self, line):
		line = str(line).encode().decode('unicode-escape') #.replace("|", "\n")
		return line.format(0.86, 0.54, "AUB", 0.62, "A")

Main()