import random
import art

decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n'    ")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
pc_cards = []
pc_1st_card = random.choice(cards)
pc_cards.append(pc_1st_card)
pc_score = sum(pc_cards)
for i in range(2):
    user_card = random.choice(cards)
    user_cards.append(user_card)
user_score = sum(user_cards)


def transform():
    global user_score
    if user_score > 21 and 11 in user_cards:
        for n in range(len(user_cards)):
            if user_cards[n] == 11:
                user_cards[n] = 1
                user_score -= 10


def current_score():
    print(f"    Your cards are :{user_cards}, current score: {user_score}")
    print(f"    Computer's first card: {pc_1st_card}")


def scores():
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {pc_cards}, final score: {pc_score}")


def pc_deck():
    global pc_score
    while pc_score < 17:
        pc_cards.append(random.choice(cards))
        pc_score = sum(pc_cards)


def comp(user_score, pc_score):
    if user_score == pc_score:
        scores()
        print("    Draw!")
    elif pc_score == 21 and len(pc_cards) == 2:
        scores()
        print("    PC wins with a Blackjack, You lose!")
    elif user_score == 21 and len(user_cards) == 2:
        scores()
        print("    You win with a Blackjack!")
    elif user_score > 21:
        scores()
        print("    You went over, you lose.")
    elif pc_score > 21:
        scores()
        print("    PC went over, You win!")
    elif user_score <= 21:
        scores()
        print("    You win!")


def game():
    transform()
    current_score()
    global user_score, user_cards, user_card
    while user_score < 21:
        hit = input("Type 'y' to get another card, type 'n' to pass: ")
        if hit == "y":
            user_card = random.choice(cards)
            user_cards.append(user_card)
            user_score = sum(user_cards)
            transform()
            current_score()
            pc_deck()
        if hit == "n":
            break
    comp(user_score, pc_score)


if decision == "y":
    print(art.logo)
    game()

while decision == "y":
    decision = input("Do you want to play another game? Type 'y' or 'n'    ")
    if decision == "y":
        game()
