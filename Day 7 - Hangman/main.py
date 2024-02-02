import random
import words
import art
print(art.logo)
end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
word_list.extend(words.word_list)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
word_letter_list = []
lives = 7
display = []
for letter in chosen_word:
    word_letter_list.append(letter)
for number in range(word_length):
    display.append("_")
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess}")
    for position in range(word_length):
        if word_letter_list[position] == guess:
            display[position] = guess
            print(display)
    if guess not in word_letter_list:
        lives -= 1
    if lives == 6:
        print(art.stages[lives])
    if lives == 5:
        print(art.stages[lives])
    if lives == 4:
        print(art.stages[lives])
    if lives == 3:
        print(art.stages[lives])
    if lives == 2:
        print(art.stages[lives])
    if lives == 1:
        print(art.stages[lives])
    if lives == 0:
        print(art.stages[lives])
        print("You lose.")
        break
    if "_" not in display:
        end_of_game = True
        print("You win.")
