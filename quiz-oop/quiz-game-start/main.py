from question_model import *
from data import *
from quiz_brain import *

question_bank = []


for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

quiz = Brain(question_bank)
while quiz.remains():
    quiz.next_question()

print("Damn you genios eh")
print(f"Your final score was {quiz.score}/{len(question_bank)}")
