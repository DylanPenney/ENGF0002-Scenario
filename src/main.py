# CREATE WORD QUESTIONS

import random
import tkinter as tk
from tkinter import *

class Main:

# Frontend

	# GUI controls for main menu
	def __init__(self):
		# Config
		self.main_menu_text = ("Welcome to the question bank.\n"
			"This question bank consists of probability questions on two levels, "
			"those being Warm Up and Word questions.\n"
			"You also have the ability to create your own questions.")
		self.title_font = ("Arial", 24, "bold")
		self.text_font = ("Arial", 16)
		self.background_colour = "#f5f5dc" # F2F2F2" # Cultured
		self.title_colour = "#226CE0" # Celtic Blue
		self.text_colour = "#226CE0" # Celtic Blue
		self.button_colour = "white"
		self.fullscreen = False

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
		self.resize_to_normal(self.root)

		self.root.configure(bg = self.background_colour)

		# Create label
		title = Label(self.root, text = "Probability Question Bank")
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
		button_functions = [self.openStarterWindow, self.openWordWindow, self.open_create_window]
		buttons = []
		for i in range (0, len(button_names)):
			buttons.append(Button(self.root, text=button_names[i], command=button_functions[i]))
			# Button must be same colour as background otherwise werid black box appears (NO FIX bug in MACOS)
			buttons[i].configure(highlightbackground = self.background_colour, foreground = self.text_colour)
			buttons[i].pack(pady=5)

		self.root.mainloop()

	# Allows the Esc key to change main menu size
	def toggle_fullscreen(self, event=None):
		self.fullscreen = not self.fullscreen
		self.root.attributes("-fullscreen", self.fullscreen)
		if not self.fullscreen:
			self.resize_to_normal(self.root)

	def resize_to_normal(self, window, event=None):
		window.geometry(f"{self.window_width}x{self.window_height}+{self.x_coord}+{self.y_coord}")


	def openStarterWindow(self):
		self.starter_question, self.starter_solution = self.starter_question_controller()

		self.starterWindow = Toplevel(self.root)
		self.starterWindow.title("Starter Question")
		self.starterWindow.bind("<Escape>", self.toggle_fullscreen_starter)
		self.fullscreen_starter = False

		self.resize_to_normal(self.starterWindow)
		self.starterWindow.configure(background = self.background_colour)

		title = Label(self.starterWindow, text = "Starter Question")
		title.configure(font = self.title_font)
		title.configure(foreground = self.title_colour)
		title.configure(background = self.background_colour)
		title.pack(pady = 20)

		# Display Question
		question_box = Text(self.starterWindow, height = 3, width = 500, font = self.text_font, wrap=WORD)
		question_box.tag_configure("tag_name", justify='center')
		question_box.insert("1.0", self.starter_question)
		question_box.configure(foreground = self.text_colour)
		question_box.configure(background = self.background_colour)
		question_box.configure(highlightthickness = 0, borderwidth=0)
		question_box.tag_add("tag_name", "1.0", "end")
		question_box.pack(pady = 10)

		# Need to do input
		self.input_box_starter = Entry(self.starterWindow, font = self.text_font, background = 'grey')
		self.input_box_starter.pack()
		self.input_box_starter.focus_set()

		submit_button_starter = Button(self.starterWindow, text="Submit", command=self.check_answer_starter)
		submit_button_starter.configure(highlightbackground = self.background_colour, foreground = self.text_colour)
		submit_button_starter.pack(pady = 5)

		retry_button_starter = Button(self.starterWindow, text="New Question", command=self.retry_starter)
		retry_button_starter.configure(highlightbackground = self.background_colour, foreground = self.text_colour)
		retry_button_starter.pack(pady = 5)

	def retry_starter(self):
		self.starterWindow.destroy()

	def check_answer_starter(self):
		answer = float(self.input_box_starter.get())
		# Create text widget, specify size, center it and populate it
		T = Text(self.starterWindow, height = 3, width = 500, font = self.text_font, wrap=WORD)
		T.tag_configure("tag_name", justify='center')
		if (self.round_to_dp(answer, 2) == self.starter_solution):
			T.insert("1.0", "Correct")
		else:
			T.insert("1.0", "Incorrect")
		T.configure(foreground = self.text_colour)
		T.configure(background = self.background_colour)
		T.configure(highlightthickness = 0, borderwidth=0)
		T.tag_add("tag_name", "1.0", "end")
		T.pack(pady = 10)

	# Need seperate helper functions for each screen
	# Allows the Esc key to change screen size
	def toggle_fullscreen_starter(self, event=None):
		self.fullscreen_starter = not self.fullscreen_starter
		self.starterWindow.attributes("-fullscreen", self.fullscreen_starter)
		if not self.fullscreen_starter:
			self.resize_to_normal(self.starterWindow)


	def openWordWindow(self):
		self.word_question, self.word_solution = self.word_question_controller()

		self.wordWindow = Toplevel(self.root)
		self.wordWindow.title("Word Question")
		self.wordWindow.bind("<Escape>", self.toggle_fullscreen_word)
		self.fullscreen_word = False

		self.resize_to_normal(self.wordWindow)
		self.wordWindow.configure(background = self.background_colour)

		title = Label(self.wordWindow, text = "Word Question")
		title.configure(font = self.title_font)
		title.configure(foreground = self.title_colour)
		title.configure(background = self.background_colour)
		title.pack(pady = 20)

		# Display Question
		question_box = Text(self.wordWindow, height = 3, width = 500, font = self.text_font, wrap=WORD)
		question_box.tag_configure("tag_name", justify='center')
		question_box.insert("1.0", self.word_question)
		question_box.configure(foreground = self.text_colour)
		question_box.configure(background = self.background_colour)
		question_box.configure(highlightthickness = 0, borderwidth=0)
		question_box.tag_add("tag_name", "1.0", "end")
		question_box.pack(pady = 10)

		# Need to do input
		self.input_box_word = Entry(self.wordWindow, font = self.text_font, background = 'grey')
		self.input_box_word.pack()
		self.input_box_word.focus_set()

		submit_button_word = Button(self.wordWindow, text="Submit", command=self.check_answer_word)
		submit_button_word.configure(highlightbackground = self.background_colour, foreground = self.text_colour)
		submit_button_word.pack(pady = 5)

		retry_button_word = Button(self.wordWindow, text="New Question", command=self.retry_word)
		retry_button_word.configure(highlightbackground = self.background_colour, foreground = self.text_colour)
		retry_button_word.pack(pady = 5)

	def retry_word(self):
		self.wordWindow.destroy()

	def check_answer_word(self):
		answer = float(self.input_box_word.get())
		# Create text widget, specify size, center it and populate it
		T = Text(self.wordWindow, height = 3, width = 500, font = self.text_font, wrap=WORD)
		T.tag_configure("tag_name", justify='center')
		if (self.round_to_dp(answer, 2) == self.word_solution):
			T.insert("1.0", "Correct")
		else:
			T.insert("1.0", "Incorrect")
		T.configure(foreground = self.text_colour)
		T.configure(background = self.background_colour)
		T.configure(highlightthickness = 0, borderwidth=0)
		T.tag_add("tag_name", "1.0", "end")
		T.pack(pady = 10)

	# Allows the Esc key to change screen size
	def	toggle_fullscreen_word(self, event=None):
		self.fullscreen_word = not self.fullscreen_word
		self.wordWindow.attributes("-fullscreen", self.fullscreen_word)
		if not self.fullscreen_word:
			self.resize_to_normal(self.wordWindow)


	def open_create_window(self):
		self.create_window = Toplevel(self.root)
		self.create_window.title("Create Question")
		self.create_window.bind("<Escape>", self.toggle_fullscreen_create)
		self.fullscreen_create = False

		self.resize_to_normal(self.create_window)
		self.create_window.configure(background = self.background_colour)

		title = Label(self.create_window, text = "Create Question")
		title.configure(font = self.title_font)
		title.configure(foreground = self.title_colour)
		title.configure(background = self.background_colour)
		title.pack(pady = 20)

		# Create buttons
		button_names = ["Create Starter Question", "Create Word Question", "Main Menu"]
		button_functions = [self.open_create_starter_window, self.open_create_word_window, self.create_question_to_main_menu]
		buttons = []
		for i in range (0, len(button_names)):
			buttons.append(Button(self.create_window, text=button_names[i], command=button_functions[i]))
			# Button must be same colour as background otherwise werid black box appears (NO FIX bug in MACOS)
			buttons[i].configure(highlightbackground = self.background_colour, foreground = self.text_colour)
			buttons[i].pack(pady=5)

	def create_question_to_main_menu(self):
		self.create_window.destroy()

	# Allows the Esc key to change screen size
	def toggle_fullscreen_create(self, event=None):
		self.fullscreen_create = not self.fullscreen_create
		self.create_window.attributes("-fullscreen", self.fullscreen_create)
		if not self.fullscreen_create:
			self.resize_to_normal(self.create_window)


	def open_create_starter_window(self):
		self.create_starter_question, self.create_starter_solution = self.create_starter_controller()
		self.create_starter_window = Toplevel(self.create_window)
		self.create_starter_window.title("Create Warm Up Question")
		self.create_starter_window.bind("<Escape>", self.toggle_fullscreen_create_starter)

		self.fullscreen_create_starter = False
		self.resize_to_normal(self.create_starter_window)
		self.create_starter_window.configure(background = self.background_colour)

		title = Label(self.create_starter_window, text = "Create Starter Question")
		title.configure(font = self.title_font)
		title.configure(foreground = self.title_colour)
		title.configure(background = self.background_colour)
		title.pack(pady = 20)

		# A and B and A or B must be first otherwise they get replaced by A, B
		self.potential_inputs = [["AandB", "P(A ∩ B)", "AandB"], ["AorB", "P(A ∪ B)", "AorB"], ["PA", "P(A)", "A"], ["PB", "P(B)", "B"]] # [[Var in question, var in text, var in sol]]

		self.list_of_entries = []
		self.list_of_required_inputs = []

		for triple in self.potential_inputs:
			if triple[0] in self.create_starter_question:
				T = Text(self.create_starter_window, height = 3, width = 500, font = self.text_font, wrap=WORD)
				T.tag_configure("tag_name", justify='center')
				T.insert("1.0", f"Please enter a value for {triple[1]}")
				T.configure(foreground = self.text_colour)
				T.configure(background = self.background_colour)
				T.configure(highlightthickness = 0, borderwidth=0)
				T.tag_add("tag_name", "1.0", "end")
				T.pack(pady = 10)

				self.list_of_required_inputs.append(T)
				self.list_of_entries.append( (triple[0], triple[2], Entry(self.create_starter_window, font = self.text_font, background = 'grey')) )
				self.list_of_entries[-1][-1].pack() # pack cannot be within the append statement otherwise none is returned

		button_names = ["Submit", "Main Menu"]
		button_functions = [self.get_input_create_starter, self.create_starter_question_to_main_menu]
		self.create_starter_buttons = []

		for i in range(0, len(button_names)):
			self.create_starter_buttons.append(Button(self.create_starter_window, text=button_names[i], command=button_functions[i]))
			self.create_starter_buttons[i].configure(highlightbackground = self.background_colour, foreground = self.text_colour)
			self.create_starter_buttons[i].pack(pady = 5)

	def get_input_create_starter(self):

		# x = question place holder
		# y = solution place holder
		# z = user's input fo that placeholder
		for (x, y, z) in self.list_of_entries:
			self.create_starter_question = self.create_starter_question.replace(x, z.get())
			self.create_starter_solution = self.create_starter_solution.replace(y, z.get())

		self.display_question_create_starter()

	def display_question_create_starter(self):

		# Clear screen
		for entry in self.list_of_entries:
			entry[2].destroy()
		for prompt in self.list_of_required_inputs:
			prompt.destroy()
		for button in self.create_starter_buttons:
			button.destroy()

		question_box = Text(self.create_starter_window, height = 3, width = 500, font = self.text_font, wrap=WORD)
		question_box.tag_configure("tag_name", justify='center')
		question_box.insert("1.0", self.create_starter_question)
		question_box.configure(foreground = self.text_colour)
		question_box.configure(background = self.background_colour)
		question_box.configure(highlightthickness = 0, borderwidth=0)
		question_box.tag_add("tag_name", "1.0", "end")
		question_box.pack(pady = 10)

		# Need to do input
		self.input_box_create_starter = Entry(self.create_starter_window, font = self.text_font, background = 'grey')
		self.input_box_create_starter.pack()
		self.input_box_create_starter.focus_set()

		button_names = ["Submit", "New Question", "Main Menu"]
		button_functions = [self.check_answer_create_starter, self.retry_create_starter, self.create_starter_question_to_main_menu]
		buttons = []

		for i in range(0, len(button_names)):
			buttons.append(Button(self.create_starter_window, text=button_names[i], command=button_functions[i]))
			buttons[i].configure(highlightbackground = self.background_colour, foreground = self.text_colour)
			buttons[i].pack(pady = 5)

	def retry_create_starter(self):
		self.create_starter_window.destroy()

	def check_answer_create_starter(self):
		answer = float(self.input_box_create_starter.get())
		# Create text widget, specify size, center it and populate it
		T = Text(self.create_starter_window, height = 3, width = 500, font = self.text_font, wrap=WORD)
		T.tag_configure("tag_name", justify='center')
		if (self.round_to_dp(answer, 2) == self.round_to_dp(eval(self.create_starter_solution), 2)):
			T.insert("1.0", "Correct")
		else:
			T.insert("1.0", "Incorrect")
		T.configure(foreground = self.text_colour)
		T.configure(background = self.background_colour)
		T.configure(highlightthickness = 0, borderwidth=0)
		T.tag_add("tag_name", "1.0", "end")
		T.pack(pady = 10)

	# Allows the Esc key to change screen size
	def toggle_fullscreen_create_starter(self, event=None):
		self.fullscreen_create_starter = not self.fullscreen_create_starter
		self.create_starter_window.attributes("-fullscreen", self.fullscreen_create_starter)
		if not self.fullscreen_create_starter:
			self.resize_to_normal(self.create_starter_window)

	def create_starter_question_to_main_menu(self):
		self.create_starter_window.destroy()
		self.create_window.destroy()


	# Functions for allowing the user to create a word question.
	def open_create_word_window(self):
		self.create_word_question, self.create_word_solution = self.create_word_question_controller()
		print(self.create_word_question)
		self.create_word_window = Toplevel(self.create_window)
		self.create_word_window.title("Create Warm Up Question")
		self.create_word_window.bind("<Escape>", self.toggle_fullscreen_create_word)

		self.fullscreen_create_word = False
		self.resize_to_normal(self.create_word_window)
		self.create_word_window.configure(background = self.background_colour)

		title = Label(self.create_word_window, text = "Create Word Question")
		title.configure(font = self.title_font)
		title.configure(foreground = self.title_colour)
		title.configure(background = self.background_colour)
		title.pack(pady = 20)

		self.list_of_create_word_potential_inputs = ["R1", "R2"]
		self.list_of_create_word_entry_prompts = []
		self.list_of_create_word_Entry_widgets = []

		for possibility in self.list_of_create_word_potential_inputs:
			if possibility in self.create_word_question:
				T = Text(self.create_word_window, height = 3, width = 500, font = self.text_font, wrap=WORD)
				T.tag_configure("tag_name", justify='center')
				T.insert("1.0", f"Please enter a whole number")
				T.configure(foreground = self.text_colour)
				T.configure(background = self.background_colour)
				T.configure(highlightthickness = 0, borderwidth=0)
				T.tag_add("tag_name", "1.0", "end")
				T.pack(pady = 10)

				self.list_of_create_word_entry_prompts.append(T)
				self.list_of_create_word_Entry_widgets.append( (possibility, Entry(self.create_word_window, font = self.text_font, background = 'grey')) )
				self.list_of_create_word_Entry_widgets[-1][-1].pack()

		button_names = ["Submit", "Main Menu"]
		button_functions = [self.get_input_create_word, self.create_word_question_to_main_menu]
		self.create_word_buttons = []

		for i in range(0, len(button_names)):
			self.create_word_buttons.append(Button(self.create_word_window, text=button_names[i], command=button_functions[i]))
			self.create_word_buttons[i].configure(highlightbackground = self.background_colour, foreground = self.text_colour)
			self.create_word_buttons[i].pack(pady = 5)


	def get_input_create_word(self):
		
		self.replacements = []
		for (x, y) in self.list_of_create_word_Entry_widgets:
			self.create_word_question = self.create_word_question.replace(x, y.get())
			self.replacements.append(float(y.get()))

		self.display_question_create_word()

	def display_question_create_word(self):
		
		# Clear screen
		for prompt in self.list_of_create_word_entry_prompts:
			prompt.destroy()
		for widget in self.list_of_create_word_Entry_widgets:
			widget[-1].destroy()
		for button in self.create_word_buttons:
			button.destroy()

		question_box = Text(self.create_word_window, height = 3, width = 500, font = self.text_font, wrap=WORD)
		question_box.tag_configure("tag_name", justify='center')
		question_box.insert("1.0", self.create_word_question)
		question_box.configure(foreground = self.text_colour)
		question_box.configure(background = self.background_colour)
		question_box.configure(highlightthickness = 0, borderwidth=0)
		question_box.tag_add("tag_name", "1.0", "end")
		question_box.pack(pady = 10)

		# Need to do input
		self.input_box_create_word = Entry(self.create_word_window, font = self.text_font, background = 'grey')
		self.input_box_create_word.pack()
		self.input_box_create_word.focus_set()

		button_names = ["Submit", "New Question", "Main Menu"]
		button_functions = [self.check_answer_create_word, self.retry_create_word, self.create_word_question_to_main_menu]
		buttons = []

		for i in range(0, len(button_names)):
			buttons.append(Button(self.create_word_window, text=button_names[i], command=button_functions[i]))
			buttons[i].configure(highlightbackground = self.background_colour, foreground = self.text_colour)
			buttons[i].pack(pady = 5)

	def check_answer_create_word(self):
		answer = float(self.input_box_create_word.get())
		# Create text widget, specify size, center it and populate it
		T = Text(self.create_word_window, height = 3, width = 500, font = self.text_font, wrap=WORD)
		T.tag_configure("tag_name", justify='center')
		print(answer, self.create_word_solution, eval(self.create_word_solution))
		if (self.round_to_dp(answer, 2) == self.round_to_dp(eval(self.create_word_solution), 2)):
			T.insert("1.0", "Correct")
		else:
			T.insert("1.0", "Incorrect")
		T.configure(foreground = self.text_colour)
		T.configure(background = self.background_colour)
		T.configure(highlightthickness = 0, borderwidth=0)
		T.tag_add("tag_name", "1.0", "end")
		T.pack(pady = 10)

	def retry_create_word(self):
		self.create_word_window.destroy()

	# Allows the Esc key to change screen size
	def toggle_fullscreen_create_word(self, event=None):
		self.fullscreen_create_word = not self.fullscreen_create_word
		self.create_word_window.attributes("-fullscreen", self.fullscreen_create_word)
		if not self.fullscreen_create_word:
			self.resize_to_normal(self.create_word_window)

	def create_word_question_to_main_menu(self):
		self.create_word_window.destroy()
		self.create_window.destroy()

# Backend

	# Interface between get_starter_question and GUI button
	def starter_question_controller(self):

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

	# Interface between get_word_question and GUI button
	def word_question_controller(self):
		self.replacements = [random.randint(1, 10) for i in range(5)]
		pair = self.get_word_question()

		question = pair[0].replace("R1", str(self.replacements[0])).replace("R2", str(self.replacements[1]))
		solution = self.round_to_dp(eval(pair[1]), 2)
		return question, solution

	# Helper function to act between get_starter_question and frontend
	def create_starter_controller(self):

		question, solution, create_independent = self.get_starter_question()

		return question, solution

	# Helper function to act between get_word_question and frontend
	def create_word_question_controller(self):

		question, solution = self.get_word_question()

		return question, solution

	# Generates a random starter question and formula for the answer
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

	# Generates a random word question and formula for the answer
	def get_word_question(self):
		with open('../word-questions/questions.txt', 'r') as q:
			questions = q.readlines()
		with open('../word-questions/solutions.txt', 'r') as s:
			solutions = s.readlines()
		index = random.randint(0, min(len(questions), len(solutions) - 1))
		question = self.format_raw_question(questions[index])
		solution = self.format_raw_solution(solutions[index])
		return question, solution

	# Allows in text vars to be replaced by actual variables
	def format_raw_question(self, line):
		line = str(line).encode().decode('utf-8').replace('\n', '')
		return line
	
	# Allows in text vars to be replaced by actual variables
	def format_raw_solution(self, line):
		line = str(line).encode().decode('utf-8').replace('\n', '')
		return line

	# UNUSED (NOT IN GUI)
	def check_solution(self, question, solution):
		user_answer = -1 # Turn while loop into a 'do-while' loop
		print(question)
		print("Answer to two decimal places (where applicable).")
		user_answer = self.round_to_dp(float(input(">>>")), 2)
		while user_answer != solution:
			user_answer = float(input("Incorrect!\n>>>"))
		print("Correct!")

	# Python rounds to evan by default - my own rounding function
	def round_to_dp(self, val, digits=2):
		precision = 10 ** digits
		return (round(precision * val) / precision)

Main()