class QuizBrain:

    def __init__(self, question_menu):
        self.question_number = 0
        self.score = 0
        self.question_menu = question_menu

    def still_questions(self):
        return self.question_number < len(self.question_menu)

    def next_question(self):
        current_question = self.question_menu[self.question_number]
        correct_answer = current_question.answer
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)")
        self.question_number += 1
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("That's correct!")
            self.score += 1
        else:
            print("That's wrong :c")
            print(f"The correct answer was {correct_answer}.")
        print(f"Your score is {self.score}/{self.question_number}\n")

