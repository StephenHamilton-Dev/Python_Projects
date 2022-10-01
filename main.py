import os
import random
import string



# List of words for hangman game
hangman_word_list = ["Mild", "Pale", "Bake", "Time", "Pilot", "Sale", "Ride", "Able", "Kind", "Apron", "Final", "While",
                     "Became", "Radar"]

# List to hold 26 letter alphabet and store in variable
alphabet = set(string.ascii_uppercase)

# variable that saves a random word from the list
word = random.choice(hangman_word_list).upper()

# if the user is guessing a letter we need to keep track of the letters that have been guessed
guessed_letters = set()

# if the user guesses a letter correctly from the word list, keep track of that letter
letters_from_list = set(word)

lives = 6

print("WELCOME TO GENEVIEVE'S SPELLING WORD HANGMAN GAME!\n")

while len(letters_from_list) > 0 and lives > 0:

    print("So far you have guessed ", ' '.join(guessed_letters))

    word_list = [letter if letter in guessed_letters else '-' for letter in word]
    print("Current word: ", ' '.join(word_list))

    user_guess = input("Please guess and enter a letter: ").upper()
    if user_guess in alphabet - guessed_letters:
        guessed_letters.add(user_guess)
        if user_guess in letters_from_list:
            letters_from_list.remove(user_guess)

        else:
            lives = lives - 1
            print(f"Letter is not in word. You now have {lives} lives left.")

    elif user_guess in guessed_letters:
        print("You have already used that letter.")

if lives == 0:
    print(f"You lost. The word we were looking for was {word}.")
else:
    print(f"You won! You guessed the word {word}, correctly!")

os.system('PAUSE')

print("Exiting Game! To Play again, press enter and run the program again.")

os.system('PAUSE')

