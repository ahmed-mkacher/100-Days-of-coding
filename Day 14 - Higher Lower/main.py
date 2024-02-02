import art
import random
from game_data import data


def comp():
    """Chooses a competitor randomly"""
    return random.choice(data)


comp_a = comp()
comp_b = comp()
while comp_b == comp_a:
    comp_a = comp()

final_score = 0
correct = True


def compare():
    """compares followers' number of both competitors"""
    global aux
    global answer
    if comp_a['follower_count'] < comp_b['follower_count']:
        answer = 'A'
    else:
        answer = 'B'
    aux = comp_b


print(art.logo)

while correct:
    print(f"Compare A: {comp_a['name']}, a {comp_a['description']}, from {comp_a['country']}")
    print("VS")
    print(f"Against B: {comp_b['name']}, a {comp_b['description']}, from {comp_a['country']}")
    user_answer = input("Who has more followers? Type 'A' or 'B':  ").upper()
    compare()
    if user_answer != answer:
        correct = False
        print(f"Sorry, that's wrong. Final score: {final_score}")
    else:
        final_score += 1
        print(f"You are right! Current score: {final_score}")
        comp_a = aux
        comp_b = comp()
