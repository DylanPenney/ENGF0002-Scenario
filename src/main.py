import random
import tkinter as tk
from tkinter import *

class Main:

# Frontend

# GUI controls for main menu
	def __init__(self):

		# Variables for quickly changing the look of the program
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

		# Config
		self.root = tk.Tk()
		self.root.title("Probability Question Bank")
		self.root.bind("<Escape>", self.toggle_fullscreen)
		self.root.configure(bg = self.background_colour)
		self.fullscreen = False

		# Centering Window
		screen_width = self.root.winfo_screenwidth()
		screen_height = self.root.winfo_screenheight()

		self.window_height = 600
		self.window_width = 600
		self.x_coord = int((screen_width/2) - (self.window_width/2))
		self.y_coord = int((screen_height/2) - (self.window_height/2))
		self.resize_to_normal(self.root)

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
		button_names = ["Generate Warm Up Question", "Generate Word Question", "Create Your Own Question"]
		button_functions = [self.open_warm_up_window, self.open_word_window, self.open_create_window]
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
		
		# If window has been un-fullscreened,
		# window is centered and resized
		if not self.fullscreen:
			self.resize_to_normal(self.root)

	# Centers the window and sets size
	def resize_to_normal(self, window, event=None):

		window.geometry(f"{self.window_width}x{self.window_height}+{self.x_coord}+{self.y_coord}")

# Functions for allowing the user to answer a Warm Up Question.
	def open_warm_up_window(self):

		# Get question and answer templates
		self.question_warm_up, self.solution_warm_up = self.question_controller_warm_up()

		# Config
		self.window_warm_up = Toplevel(self.root)
		self.window_warm_up.title("Warm Up Question")
		self.window_warm_up.bind("<Escape>", self.toggle_fullscreen_warm_up)
		self.fullscreen_warm_up = False
		self.resize_to_normal(self.window_warm_up)
		self.window_warm_up.configure(background = self.background_colour)

		# Create label
		title_warm_up = Label(self.window_warm_up, text = "Warm Up Question")
		title_warm_up.configure(font = self.title_font)
		title_warm_up.configure(foreground = self.title_colour)
		title_warm_up.configure(background = self.background_colour)
		title_warm_up.pack(pady = 20)

		# Display Question
		question_box_warm_up = Text(self.window_warm_up, height = 3, width = 500, font = self.text_font, wrap=WORD)
		question_box_warm_up.tag_configure("tag_name", justify='center')
		question_box_warm_up.insert("1.0", self.question_warm_up)
		question_box_warm_up.configure(foreground = self.text_colour)
		question_box_warm_up.configure(background = self.background_colour)
		question_box_warm_up.configure(highlightthickness = 0, borderwidth=0)
		question_box_warm_up.tag_add("tag_name", "1.0", "end")
		question_box_warm_up.pack(pady = 10)

		# User input
		self.input_box_warm_up = Entry(self.window_warm_up, font = self.text_font, background = 'grey')
		self.input_box_warm_up.pack()
		self.input_box_warm_up.focus_set()

		# Create buttons
		button_names_warm_up = ["Submit", "New Question"]
		button_functions_warm_up = [self.check_answer_warm_up, self.retry_warm_up]
		buttons_warm_up = []

		for i in range(0, len(button_names_warm_up)):
			
			buttons_warm_up.append(Button(self.window_warm_up, text=button_names_warm_up[i], command=button_functions_warm_up[i]))
			buttons_warm_up[i].configure(highlightbackground = self.background_colour, foreground = self.text_colour)
			buttons_warm_up[i].pack(pady=5)

	# Allows user to reselect question type
	def retry_warm_up(self):

		self.window_warm_up.destroy()

	# Checks and displays whether user's answer is correct
	def check_answer_warm_up(self):

		# Gets user's answer from input box
		answer_warm_up = float(self.input_box_warm_up.get())

		# Create text widget, specify size, center it and populate it
		T_warm_up = Text(self.window_warm_up, height = 3, width = 500, font = self.text_font, wrap=WORD)
		T_warm_up.tag_configure("tag_name", justify='center')
		
		# Displays "Correct" if user's answer is within 0.005 of the correct answer,
		# otherwise "Incorrect"
		if (self.round_to_dp(answer_warm_up, 2) == self.solution_warm_up):
			T_warm_up.insert("1.0", "Correct")
		else:
			T_warm_up.insert("1.0", "Incorrect")
		
		T_warm_up.configure(foreground = self.text_colour)
		T_warm_up.configure(background = self.background_colour)
		T_warm_up.configure(highlightthickness = 0, borderwidth=0)
		T_warm_up.tag_add("tag_name", "1.0", "end")
		T_warm_up.pack(pady = 10)

	# Need seperate helper functions for each window
	# Allows the Esc key to change window size
	def toggle_fullscreen_warm_up(self, event=None):

		self.fullscreen_warm_up = not self.fullscreen_warm_up
		self.window_warm_up.attributes("-fullscreen", self.fullscreen_warm_up)
		
		# If window has been un-fullscreened,
		# window is centered and resized
		if not self.fullscreen_warm_up:
			self.resize_to_normal(self.window_warm_up)

# Functions for allowing the user to answer a Word Question
	def open_word_window(self):

		# Get question and answer templates
		self.question_word, self.solution_word = self.question_controller_word()

		# Config
		self.window_word = Toplevel(self.root)
		self.window_word.title("Word Question")
		self.window_word.bind("<Escape>", self.toggle_fullscreen_word)
		self.fullscreen_word = False
		self.resize_to_normal(self.window_word)
		self.window_word.configure(background = self.background_colour)

		# Create label
		title_word = Label(self.window_word, text = "Word Question")
		title_word.configure(font = self.title_font)
		title_word.configure(foreground = self.title_colour)
		title_word.configure(background = self.background_colour)
		title_word.pack(pady = 20)

		# Display question
		question_box_word = Text(self.window_word, height = 3, width = 500, font = self.text_font, wrap=WORD)
		question_box_word.tag_configure("tag_name", justify='center')
		question_box_word.insert("1.0", self.question_word)
		question_box_word.configure(foreground = self.text_colour)
		question_box_word.configure(background = self.background_colour)
		question_box_word.configure(highlightthickness = 0, borderwidth=0)
		question_box_word.tag_add("tag_name", "1.0", "end")
		question_box_word.pack(pady = 10)

		# User input
		self.input_box_word = Entry(self.window_word, font = self.text_font, background = 'grey')
		self.input_box_word.pack()
		self.input_box_word.focus_set()

		# Create Buttons
		button_names_word = ["Submit", "New Question"]
		button_functions_word = [self.check_answer_word, self.retry_word]
		buttons_word = []

		for i in range(0, len(button_names_word)):
			buttons_word.append(Button(self.window_word, text=button_names_word[i], command=button_functions_word[i]))
			buttons_word[i].configure(highlightbackground = self.background_colour, foreground = self.text_colour)
			buttons_word[i].pack(pady = 5)

	# Allows user to reselect question type
	def retry_word(self):

		self.window_word.destroy()

	# Checks and displays whether user's answer is correct
	def check_answer_word(self):

		# Gets user's answer from input box
		answer_word = float(self.input_box_word.get())

		# Create text widget, specify size, center it and populate it
		T_word = Text(self.window_word, height = 3, width = 500, font = self.text_font, wrap=WORD)
		T_word.tag_configure("tag_name", justify='center')
		
		# Displays "Correct" if user's answer is within 0.005 of the correct answer,
		# otherwise "Incorrect"
		if (self.round_to_dp(answer_word, 2) == self.solution_word):
			T_word.insert("1.0", "Correct")
		else:
			T_word.insert("1.0", "Incorrect")
		
		T_word.configure(foreground = self.text_colour)
		T_word.configure(background = self.background_colour)
		T_word.configure(highlightthickness = 0, borderwidth=0)
		T_word.tag_add("tag_name", "1.0", "end")
		T_word.pack(pady = 10)

	# Allows the Esc key to change screen size
	def	toggle_fullscreen_word(self, event=None):

		self.fullscreen_word = not self.fullscreen_word
		self.window_word.attributes("-fullscreen", self.fullscreen_word)

		# If window has been un-fullscreened,
		# window is centered and resized
		if not self.fullscreen_word:
			self.resize_to_normal(self.window_word)

# Functions for allowing the user to create questions
	def open_create_window(self):

		# Config
		self.window_create = Toplevel(self.root)
		self.window_create.title("Create Question")
		self.window_create.bind("<Escape>", self.toggle_fullscreen_create)
		self.fullscreen_create = False
		self.resize_to_normal(self.window_create)
		self.window_create.configure(background = self.background_colour)

		# Create label
		title_create = Label(self.window_create, text = "Create Question")
		title_create.configure(font = self.title_font)
		title_create.configure(foreground = self.title_colour)
		title_create.configure(background = self.background_colour)
		title_create.pack(pady = 20)

		# Create buttons
		button_names_create = ["Create Warm Up Question", "Create Word Question", "Main Menu"]
		button_functions_create = [self.open_create_window_warm_up, self.open_create_window_word, self.create_question_to_main_menu]
		buttons_create = []
		
		for i in range (0, len(button_names_create)):

			buttons_create.append(Button(self.window_create, text=button_names_create[i], command=button_functions_create[i]))
			buttons_create[i].configure(highlightbackground = self.background_colour, foreground = self.text_colour)
			buttons_create[i].pack(pady=5)

	# Method that 'sends' user to main menu
	def create_question_to_main_menu(self):

		self.window_create.destroy()

	# Allows the Esc key to change screen size
	def toggle_fullscreen_create(self, event=None):

		self.fullscreen_create = not self.fullscreen_create
		self.window_create.attributes("-fullscreen", self.fullscreen_create)
		
		# If window has been un-fullscreened,
		# window is centered and resized
		if not self.fullscreen_create:
			self.resize_to_normal(self.window_create)

# Functions for allowing the user to create a Warm Up Question
	def open_create_window_warm_up(self):

		# Get question and answer templates
		self.question_create_warm_up, self.solution_create_warm_up = self.create_controller_warm_up()
		
		# Config
		self.window_create_warm_up = Toplevel(self.window_create)
		self.window_create_warm_up.title("Create Warm Up Question")
		self.window_create_warm_up.bind("<Escape>", self.toggle_fullscreen_create_warm_up)
		self.fullscreen_create_warm_up = False
		self.resize_to_normal(self.window_create_warm_up)
		self.window_create_warm_up.configure(background = self.background_colour)

		# Create label
		title_create_warm_up = Label(self.window_create_warm_up, text = "Create Warm Up Question")
		title_create_warm_up.configure(font = self.title_font)
		title_create_warm_up.configure(foreground = self.title_colour)
		title_create_warm_up.configure(background = self.background_colour)
		title_create_warm_up.pack(pady = 20)

		# A and B and A or B must be first otherwise they get replaced by A, B
		# [[Variable in question, variable in text, variable in sol]]
		self.potential_inputs_create_warm_up = [["AandB", "P(A ∩ B)", "AandB"], ["AorB", "P(A ∪ B)", "AorB"], ["PA", "P(A)", "A"], ["PB", "P(B)", "B"]]

		# Storing widgets
		self.list_of_Entry_widgets_create_warm_up = []
		self.list_of_entry_prompts_create_warm_up = []

		# Get user's values for the required variable
		for triple in self.potential_inputs_create_warm_up:

			if triple[0] in self.question_create_warm_up:
				T = Text(self.window_create_warm_up, height = 3, width = 500, font = self.text_font, wrap=WORD)
				T.tag_configure("tag_name", justify='center')
				T.insert("1.0", f"Please enter a value for {triple[1]}")
				T.configure(foreground = self.text_colour)
				T.configure(background = self.background_colour)
				T.configure(highlightthickness = 0, borderwidth=0)
				T.tag_add("tag_name", "1.0", "end")
				T.pack(pady = 10)

				self.list_of_entry_prompts_create_warm_up.append(T)
				self.list_of_Entry_widgets_create_warm_up.append( (triple[0], triple[2], Entry(self.window_create_warm_up, font = self.text_font, background = 'grey')) )
				self.list_of_Entry_widgets_create_warm_up[-1][-1].pack() # Pack cannot be within the append statement otherwise none is returned

		# Create buttons
		button_names_create_warm_up = ["Submit", "Main Menu"]
		button_functions_create_warm_up = [self.get_input_create_warm_up, self.create_warm_up_question_to_main_menu]
		self.buttons_create_warm_up = []

		for i in range(0, len(button_names_create_warm_up)):

			self.buttons_create_warm_up.append(Button(self.window_create_warm_up, text=button_names_create_warm_up[i], command=button_functions_create_warm_up[i]))
			self.buttons_create_warm_up[i].configure(highlightbackground = self.background_colour, foreground = self.text_colour)
			self.buttons_create_warm_up[i].pack(pady = 5)

	# Method that gets the users values and,
	# inserts them into question and answer formula
	def get_input_create_warm_up(self):

		# x = question place holder
		# y = solution place holder
		# z = user's input for that placeholder
		for (x, y, z) in self.list_of_Entry_widgets_create_warm_up:

			self.question_create_warm_up = self.question_create_warm_up.replace(x, z.get())
			self.solution_create_warm_up = self.solution_create_warm_up.replace(y, z.get())

		self.display_question_create_warm_up()

	# Method that clears the window and displays the question for the user
	def display_question_create_warm_up(self):

		# Clear screen
		for entry in self.list_of_Entry_widgets_create_warm_up:

			entry[2].destroy()

		for prompt in self.list_of_entry_prompts_create_warm_up:

			prompt.destroy()

		for button in self.buttons_create_warm_up:

			button.destroy()

		# Display question
		question_box_create_warm_up = Text(self.window_create_warm_up, height = 3, width = 500, font = self.text_font, wrap=WORD)
		question_box_create_warm_up.tag_configure("tag_name", justify='center')
		question_box_create_warm_up.insert("1.0", self.question_create_warm_up)
		question_box_create_warm_up.configure(foreground = self.text_colour)
		question_box_create_warm_up.configure(background = self.background_colour)
		question_box_create_warm_up.configure(highlightthickness = 0, borderwidth=0)
		question_box_create_warm_up.tag_add("tag_name", "1.0", "end")
		question_box_create_warm_up.pack(pady = 10)

		# User input
		self.input_box_create_warm_up = Entry(self.window_create_warm_up, font = self.text_font, background = 'grey')
		self.input_box_create_warm_up.pack()
		self.input_box_create_warm_up.focus_set()

		# Create buttons
		button_names_create_warm_up = ["Submit", "New Question", "Main Menu"]
		button_functions_create_warm_up = [self.check_answer_create_warm_up, self.retry_create_warm_up, self.create_warm_up_question_to_main_menu]
		buttons_create_warm_up = []

		for i in range(0, len(button_names_create_warm_up)):

			buttons_create_warm_up.append(Button(self.window_create_warm_up, text=button_names_create_warm_up[i], command=button_functions_create_warm_up[i]))
			buttons_create_warm_up[i].configure(highlightbackground = self.background_colour, foreground = self.text_colour)
			buttons_create_warm_up[i].pack(pady = 5)

	# Allows user to reselct question type
	def retry_create_warm_up(self):

		self.window_create_warm_up.destroy()

	# Checks and displays whether user's answer is correct
	def check_answer_create_warm_up(self):

		# Gets user's answer from input box
		answer_create_warm_up = float(self.input_box_create_warm_up.get())

		# Create text widget, specify size, center it and populate it
		T_create_warm_up = Text(self.window_create_warm_up, height = 3, width = 500, font = self.text_font, wrap=WORD)
		T_create_warm_up.tag_configure("tag_name", justify='center')

		# Displays "Correct" if user's answer is within 0.005 of the correct answer,
		# otherwise "Incorrect"
		if (self.round_to_dp(answer_create_warm_up, 2) == self.round_to_dp(eval(self.solution_create_warm_up), 2)):
			T_create_warm_up.insert("1.0", "Correct")
		else:
			T_create_warm_up.insert("1.0", "Incorrect")

		T_create_warm_up.configure(foreground = self.text_colour)
		T_create_warm_up.configure(background = self.background_colour)
		T_create_warm_up.configure(highlightthickness = 0, borderwidth=0)
		T_create_warm_up.tag_add("tag_name", "1.0", "end")
		T_create_warm_up.pack(pady = 10)

	# Allows the Esc key to change screen size
	def toggle_fullscreen_create_warm_up(self, event=None):

		self.fullscreen_create_warm_up = not self.fullscreen_create_warm_up
		self.window_create_warm_up.attributes("-fullscreen", self.fullscreen_create_warm_up)
		
		# If window has been un-fullscreened,
		# window is centered and resized
		if not self.fullscreen_create_warm_up:
			self.resize_to_normal(self.window_create_warm_up)

	# Method that 'sends' user to main menu
	def create_warm_up_question_to_main_menu(self):

		self.window_create_warm_up.destroy()
		self.window_create.destroy()

# Functions for allowing the user to create a Word Question
	def open_create_window_word(self):

		# Get question and answer templates
		self.question_create_word, self.solution_create_word = self.create_controller_word_question()

		# Config
		self.window_create_word = Toplevel(self.window_create)
		self.window_create_word.title("Create Warm Up Question")
		self.window_create_word.bind("<Escape>", self.toggle_fullscreen_create_word)
		self.fullscreen_create_word = False
		self.resize_to_normal(self.window_create_word)
		self.window_create_word.configure(background = self.background_colour)

		# Create Label
		title_create_word = Label(self.window_create_word, text = "Create Word Question")
		title_create_word.configure(font = self.title_font)
		title_create_word.configure(foreground = self.title_colour)
		title_create_word.configure(background = self.background_colour)
		title_create_word.pack(pady = 20)

		# [Variable in question/solution]
		self.potential_inputs_create_word = ["R1", "R2"]
		
		# Storing widgets
		self.list_of_entry_prompts_create_word = []
		self.list_of_Entry_widgets_create_word = []

		# Get user's values for the required variable
		for possibility in self.potential_inputs_create_word:

			if possibility in self.question_create_word:
				T = Text(self.window_create_word, height = 3, width = 500, font = self.text_font, wrap=WORD)
				T.tag_configure("tag_name", justify='center')
				T.insert("1.0", f"Please enter a whole number")
				T.configure(foreground = self.text_colour)
				T.configure(background = self.background_colour)
				T.configure(highlightthickness = 0, borderwidth=0)
				T.tag_add("tag_name", "1.0", "end")
				T.pack(pady = 10)

				self.list_of_entry_prompts_create_word.append(T)
				self.list_of_Entry_widgets_create_word.append( (possibility, Entry(self.window_create_word, font = self.text_font, background = 'grey')) )
				self.list_of_Entry_widgets_create_word[-1][-1].pack()

		# Create buttons
		button_names_create_word = ["Submit", "Main Menu"]
		button_functions_create_word = [self.get_input_create_word, self.create_word_question_to_main_menu]
		self.buttons_create_word = []

		for i in range(0, len(button_names_create_word)):

			self.buttons_create_word.append(Button(self.window_create_word, text=button_names_create_word[i], command=button_functions_create_word[i]))
			self.buttons_create_word[i].configure(highlightbackground = self.background_colour, foreground = self.text_colour)
			self.buttons_create_word[i].pack(pady = 5)

	# Method that gets the users values and,
	# inserts them into question and answer formula
	def get_input_create_word(self):
		
		# Stores users values for placeholders
		self.replacements = []

		# x = question placeholder
		# y = user's input for that placeholder
		for (x, y) in self.list_of_Entry_widgets_create_word:

			self.question_create_word = self.question_create_word.replace(x, y.get())
			self.replacements.append(float(y.get()))

		self.display_question_create_word()

	# Method that clears the window and displays the question for the user
	def display_question_create_word(self):
		
		# Clear screen
		for prompt in self.list_of_entry_prompts_create_word:

			prompt.destroy()
		
		for widget in self.list_of_Entry_widgets_create_word:
		
			widget[-1].destroy()
		
		for button in self.buttons_create_word:
		
			button.destroy()

		# Display question
		question_box_create_word = Text(self.window_create_word, height = 3, width = 500, font = self.text_font, wrap=WORD)
		question_box_create_word.tag_configure("tag_name", justify='center')
		question_box_create_word.insert("1.0", self.question_create_word)
		question_box_create_word.configure(foreground = self.text_colour)
		question_box_create_word.configure(background = self.background_colour)
		question_box_create_word.configure(highlightthickness = 0, borderwidth=0)
		question_box_create_word.tag_add("tag_name", "1.0", "end")
		question_box_create_word.pack(pady = 10)

		# User input
		self.input_box_create_word = Entry(self.window_create_word, font = self.text_font, background = 'grey')
		self.input_box_create_word.pack()
		self.input_box_create_word.focus_set()

		# Create buttons
		button_names_create_word = ["Submit", "New Question", "Main Menu"]
		button_functions_create_word = [self.check_answer_create_word, self.retry_create_word, self.create_word_question_to_main_menu]
		buttons_create_word = []

		for i in range(0, len(button_names_create_word)):

			buttons_create_word.append(Button(self.window_create_word, text=button_names_create_word[i], command=button_functions_create_word[i]))
			buttons_create_word[i].configure(highlightbackground = self.background_colour, foreground = self.text_colour)
			buttons_create_word[i].pack(pady = 5)

	# Checks and displays whether user's answer is correct
	def check_answer_create_word(self):

		# Gets user's answer from input box
		answer_create_word = float(self.input_box_create_word.get())

		# Create text widget, specify size, center it and populate it
		T_create_word = Text(self.window_create_word, height = 3, width = 500, font = self.text_font, wrap=WORD)
		T_create_word.tag_configure("tag_name", justify='center')
		
		# Displays "Correct" if user's answer is within 0.005 of the correct answer,
		# otherwise "Incorrect"
		if (self.round_to_dp(answer_create_word, 2) == self.round_to_dp(eval(self.solution_create_word), 2)):
			T_create_word.insert("1.0", "Correct")
		else:
			T_create_word.insert("1.0", "Incorrect")
		
		T_create_word.configure(foreground = self.text_colour)
		T_create_word.configure(background = self.background_colour)
		T_create_word.configure(highlightthickness = 0, borderwidth=0)
		T_create_word.tag_add("tag_name", "1.0", "end")
		T_create_word.pack(pady = 10)

	# Allows user to reselect question type
	def retry_create_word(self):

		self.window_create_word.destroy()

	# Allows the Esc key to change screen size
	def toggle_fullscreen_create_word(self, event=None):
		
		self.fullscreen_create_word = not self.fullscreen_create_word
		self.window_create_word.attributes("-fullscreen", self.fullscreen_create_word)
		
		# If window has been un-fullscreened,
		# window is centered and resized		
		if not self.fullscreen_create_word:
			self.resize_to_normal(self.window_create_word)

	# Method that 'sends' user to main menu
	def create_word_question_to_main_menu(self):
		
		self.window_create_word.destroy()
		self.window_create.destroy()

# Backend

	# Interface between get_question_warm_up and GUI buttons
	def question_controller_warm_up(self):

		# Gets details about question (question, formula, dependent/independent events)
		data = self.get_question_warm_up()
		
		# Determines whether events are independent or dependent
		independent_event = (data[2] == "independent")

		# Generate random variables to be inserted
		A = self.round_to_dp(random.uniform(0.1, 1.0), 2)
		B = self.round_to_dp(random.uniform(0.1, 1.0), 2)

		# P(A ∩ B) is only var to differ based on whether independent/dependent
		if (independent_event):
			# for independent events only
			AandB = self.round_to_dp(A * B, 2)
			AorB = self.round_to_dp(A + B - AandB, 2)
		else:
			# dependent events
			AorB = -1

			# Due to random element in P(A ∩ B) for dependent events
			while (AorB < max(A, B)) or (AorB > 1):
				
				AandB = self.round_to_dp(B * random.uniform(0.01, 1), 2) # P(A | B) = P(A ∩ B) / P(B) --> P(A ∩ B) = P(B) * P(A | B)
				AorB = self.round_to_dp(A + B - AandB, 2)
			
		# Inserts the generated variables into the question body
		question = data[0].replace("PA", str(A)).replace("PB", str(B)).replace("AorB", str(AorB)).replace("AandB", str(AandB)) # String formatting
		
		# Calculates a numerical answer
		solution = self.round_to_dp(eval(data[1]), 2)
		
		return question, solution

	# Interface between get_word_question and GUI buttons
	def question_controller_word(self):
		
		# Generate random variables to be inserted
		self.replacements = [random.randint(1, 10) for i in range(5)]

		# Get details about question (question, formula)
		data = self.get_question_word()

		# Inserts the generated variables into the question body
		question = data[0].replace("R1", str(self.replacements[0])).replace("R2", str(self.replacements[1]))
		
		# Calculates a numerical answer
		solution = self.round_to_dp(eval(data[1]), 2)
		
		return question, solution

	# Helper function to act between get_question_warm_up and frontend 
	# when user creates a question
	def create_controller_warm_up(self):

		question, solution, create_independent = self.get_question_warm_up()

		return question, solution

	# Helper function to act between get_word_question and frontend
	# when user creates a question
	def create_controller_word_question(self):

		question, solution = self.get_question_word()

		return question, solution

	# Generates a random Warm Up question and formula for the answer
	def get_question_warm_up(self):
		
		# Reads all possible question and formula templates
		with open('../warm-up-questions/warm-up-questions.txt', 'r') as q:
			questions = q.readlines()
		with open('../warm-up-questions/warm-up-solutions.txt', 'r') as s:
			solutions = s.readlines()

		# Picks a random question
		index = random.randint(0, min(len(questions), len(solutions) - 1))
		question = self.format_raw_question(questions[index])
		solution = self.format_raw_solution(solutions[index])
		
		# Determines whether events are independent or dependent
		if "independent" in question:
			return question, solution, "independent"
		else:
			return question, solution, "dependent"

	# Generates a random word question and formula for the answer
	def get_question_word(self):
		
		# Reads all possible question and formula templates
		with open('../word-questions/questions.txt', 'r') as q:
			questions = q.readlines()
		with open('../word-questions/solutions.txt', 'r') as s:
			solutions = s.readlines()
		
		# Pciks a random question
		index = random.randint(0, min(len(questions), len(solutions) - 1))
		question = self.format_raw_question(questions[index])
		solution = self.format_raw_solution(solutions[index])
		
		return question, solution

	# Allows in text variables to be replaced by actual variables
	def format_raw_question(self, line):
		
		line = str(line).encode().decode('utf-8').replace('\n', '')
		
		return line
	
	# Allows in text variables to be replaced by actual variables
	def format_raw_solution(self, line):
		
		line = str(line).encode().decode('utf-8').replace('\n', '')
		
		return line

	# Python rounds to evan by default - my own rounding function
	def round_to_dp(self, val, digits=2):
		
		precision = 10 ** digits
		
		# Truncates remainder
		return (round(precision * val) / precision)

Main()