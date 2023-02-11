from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg = THEME_COLOR, padx = 20 , pady = 20)
        self.score = Label(text = "Score : 0", background = THEME_COLOR, fg = "white")
        self.score.grid(row = 0, column = 1)
        self.canvas = Canvas(width = 300, height = 250)
        self.questiontext = self.canvas.create_text(150,125, width = 280,  text = "" , font = ("Ariel", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row = 1, column = 0 , columnspan = 2, pady=50)
        correctimg = PhotoImage(file="images/true.png")
        self.correct = Button(image = correctimg, highlightthickness= 0, command = self.true_pressed)
        self.correct.grid(row = 2, column = 0) 
        falseimg = PhotoImage(file = "images/false.png")
        self.false = Button(image = falseimg, highlightthickness = 0 , command = self.false_pressed)
        self.false.grid(row = 2, column = 1)
        self.get_next_q()
        self.window.mainloop()

    def get_next_q(self):
        self.canvas.config(bg = "white")
        if self.quiz.still_has_questions():
            self.score.config(text = f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questiontext, text = q_text)
        else:
            self.canvas.itemconfig(self.questiontext, text = f"You completed the quiz.\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.correct.config(state = "disabled")
            self.false.config(state = "disabled")
    
    def true_pressed(self):
        isright = self.quiz.check_answer("True")
        self.give_feedback(isright)

    def false_pressed(self):
        isright = self.quiz.check_answer("False")
        self.give_feedback(isright)
    
    def give_feedback(self, isright):
        if isright:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, self.get_next_q)

