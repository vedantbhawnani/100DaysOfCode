from data import *
from question_model import *


class Brain:
    def __init__(self, question_bank) -> None:
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.user = input(f"Q{self.question_number} {current_question.text} ")
        self.check_answer(self.user, current_question.answer)

    def remains(self):
        self.len = len(self.question_list)
        return self.len > self.question_number

    def check_answer(self, user_answer, correct):
        global score
        if user_answer.lower() == correct.lower():
            print("COrrect answer!")
            self.score += 1
        else:
            print("Bzzzz")
            print(f"The correct answer was {correct}")
        print(f"Your score is {self.score}/{self.question_number}")