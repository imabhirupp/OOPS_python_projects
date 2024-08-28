import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):                                                                                      # Checking if the question number is less than the length of the question_list
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]                                                # Current question is equal to the question from the question_list of the current question number
        self.question_number += 1                                                                                       # Increasing the question number each time to access the next question in the next time
        question_text = html.unescape(self.current_question.text)                                                       # Saving and formating the question to unescape html entities
        return f"Q.{self.question_number}: {question_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():                                                               # Checking if the answer is correct
            self.score += 1                                                                                             # If answer is correct then score increases by 1
            return True
        else:
            return False