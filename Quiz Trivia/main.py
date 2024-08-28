from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import Quiz_UI

question_bank = []
for question in question_data:                                                                                          # Looping through all the questions in the question_list
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = Quiz_UI(quiz)                                                                                                 # Calling quiz_ui with the quiz parameter

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
