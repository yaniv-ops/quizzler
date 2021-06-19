import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quizbrain: QuizBrain ):
        self.quiz = quizbrain
        self.window = tk.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text='Score : 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='Some question', width=280,
                                                     fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true_img = tk.PhotoImage(file='/home/tamar-alter/PycharmProjects/quizzler/images/true.png')
        false_img = tk.PhotoImage(file='/home/tamar-alter/PycharmProjects/quizzler/images/false.png')
        self.true_button = tk.Button(image=true_img,  highlightthickness=0, bg=THEME_COLOR, command = self.true_pressed)
        self.false_button = tk.Button(image=false_img, bg=THEME_COLOR, highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(column=1, row=2)
        self.false_button.grid(column=0, row=2)
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="It's the end of the quiz")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):
        self.get_feedback( self.quiz.check_answer('True'))

    def false_pressed(self):
        self.get_feedback(self.quiz.check_answer('False'))

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
