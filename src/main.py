import random

from tkinter import *
import tkinter as tk

class Main:
	def __init__(self):

		# Config
		self.main_menu_text = ("Welcome to the question bank.\n"
			"This question bank consists of probability questions on two levels, "
			"those being Warm Up and Word questions.\n"
			"You also have the ability to create your own questions."
			)
		self.title_font = ("Arial", 24, "bold")
		self.text_font = ("Arial", 16)
		self.background_colour = "#f5f5dc" # F2F2F2" # Cultured
		self.title_colour = "#226CE0" # Celtic Blue
		self.text_colour = "#226CE0" # Celtic Blue
		self.button_colour = "white"

		self.root = tk.Tk()
		self.root.title("Probability Question Bank")
		self.root.bind("<Escape>", self.toggle_fullscreen)

		# Centering Window
		self.window_height = 600
		self.window_width = 600
		screen_width = self.root.winfo_screenwidth()
		screen_height = self.root.winfo_screenheight()
		self.x_coord = int((screen_width/2) - (self.window_width/2))
		self.y_coord = int((screen_height/2) - (self.window_height/2))
		self.resize_to_normal()

		self.root.configure(bg = self.background_colour)
		self.notfullscreen = False

		# Create label
		title = Label(self.root, text = "Maths Question Bank")
		title.configure(font = self.title_font)
		title.configure(foreground = self.title_colour)
		title.configure(background = self.background_colour)
		title.pack(pady = 20)

		# Create text widget, specify size, center it and populate it
		T = Text(self.root, height = 3, width = 500, font = self.text_font, wrap=WORD)
		T.tag_configure("tag_name", justify='center')
		T.insert("1.0", self.main_menu_text)
		T.configure(foreground = self.text_colour)
		T.configure(background = self.background_colour)
		T.configure(highlightthickness = 0, borderwidth=0)
		T.tag_add("tag_name", "1.0", "end")
		T.pack(pady = 10)

	 	# Create buttons
		button_names = ["Generate Starter Question", "Generate Word Question", "Create Your Own Question"]
		button_functions = [self.openStarterWindow, self.root.destroy, self.root.destroy]
		buttons = []
		for i in range (0, 3):
			buttons.append(Button(self.root, text=button_names[i], command=button_functions[i]))
			# Button must be same colour as background otherwise werid black box appears (NO FIX bug in MACOS)
			buttons[i].configure(highlightbackground = self.background_colour, foreground = self.text_colour)
			buttons[i].pack(pady=5)

		self.root.mainloop()

	def toggle_fullscreen(self, event=None):
		self.notfullscreen = not self.notfullscreen
		self.root.attributes("-fullscreen", self.notfullscreen)
		if not self.notfullscreen:
			self.resize_to_normal()

	def resize_to_normal(self, event=None):
		self.root.geometry(f"{self.window_width}x{self.window_height}+{self.x_coord}+{self.y_coord}")

	def openStarterWindow(self):
			response = self.starter_question()
			question = response[0]
			answer = response[1]
			starterWindow = Toplevel(self.root)
			starterWindow.title("Starter Question")
			starterWindow.geometry("500x500")
			Label(starterWindow, text = f"Starter Question: {self.starter_question()}").pack()

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
			while (AorB < max(A, B)) or (AorB > 1): # Due to random element in P(A ∩ B) for dependent events
				AandB = self.round_to_dp(B * random.uniform(0.01, 1), 2) # P(A | B) = P(A ∩ B) / P(B) --> P(A ∩ B) = P(B) * P(A | B)
				AorB = self.round_to_dp(A + B - AandB, 2)
			
		question = data[0].replace("PA", str(A)).replace("PB", str(B)).replace("AorB", str(AorB)).replace("AandB", str(AandB)) # String formatting
		solution = self.round_to_dp(eval(data[1]), 2)
		
		return question, solution

	# Acts as a menu for questions (word)
	def word_question(self):
		random_numbers = [random.randint(1, 10) for i in range(5)]
		pair = self.get_word_question()

		question = pair[0].replace("R1", str(random_numbers[0])).replace("R2", str(random_numbers[1]))
		solution = self.round_to_dp(eval(pair[1]), 2)
		self.check_solution(question, solution)

	# Provides interface with a random question and answer from the selection of warm up questions
	def get_starter_question(self):
		with open('../warm-up-questions/starter-questions.txt', 'r') as q:
			questions = q.readlines()
		with open('../warm-up-questions/starter-solutions.txt', 'r') as s:
			solutions = s.readlines()
		index = random.randint(0, min(len(questions), len(solutions) - 1))
		question = self.format_raw_question(questions[index])
		solution = self.format_raw_solution(solutions[index])
		if "independent" in question:
			return question, solution, "independent"
		else:
			return question, solution, "dependent"

	def get_word_question(self):
		with open('../word-questions/questions.txt', 'r') as q:
			questions = q.readlines()
		with open('../word-questions/solutions.txt', 'r') as s:
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