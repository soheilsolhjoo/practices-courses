# Day 7 Exercise
# 100 Days of Code (Udemy)

import random
import os

from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Clear screen and show the logo
os.system("cls")  # Windows
# os.system("clear")  # Linux
print(logo)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = word_length * ["_"]

all_guesses = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("You can guess only one letter.")
        continue
    if not guess.isalpha():
        print("Your guess must be a letter of alphabet.")
        continue
    if guess in all_guesses:
        print(f"You've already guessed '{guess}'. Try a new letter.")
        continue

    all_guesses += guess
    all_guesses = list(set(all_guesses))

    os.system("cls")  # Windows
    # os.system("clear")  # Linux
    print(logo)

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
