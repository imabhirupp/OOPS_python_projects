from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quiz_UI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question = self.canvas.create_text(150, 125, width=280, text="Some Question", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)                                                        # pady=50 so that to shift the elements a bit upward and downward and create space between the items

        wrong_image = PhotoImage(file="images/false.png")                                                               # These are not self. because we won't be needing to access these from anywhere else in the class
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.right_pressed)
        self.wrong_button.grid(column=1, row=2)

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.wrong_pressed)
        self.right_button.grid(column=0, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):                                                                                        # Changing to the next question
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():                                                                             # Checking if there are questions left in the question bank
            self.score_label.config(text=f"Score: {self.quiz.score}")                                                   # Changing the score with each correct answer
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="No More Questions left.")                                       # When there are no questions left, display the text
            self.right_button.config(state="disabled")                                                                  # Disabling the button animation when the quiz ends
            self.wrong_button.config(state="disabled")                                                                  # Disabling the button animation when the quiz ends
    def right_pressed(self, ):                                                                                          # Checks if the true pressed is same as the answer of the question
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_pressed(self):                                                                                            # Checks if the false pressed is same as the answer of the question
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)                                                             # After 1000ms the question changes
