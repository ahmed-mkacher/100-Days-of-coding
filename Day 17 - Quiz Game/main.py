from data import *
from question_model import *
from quiz_brain import *

question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_questions():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score is {quiz.score}/{quiz.question_number}")