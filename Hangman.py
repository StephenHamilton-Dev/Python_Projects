import random
import string
from words import words

# function to get a valid word from the list words.py
def get_valid_word(words):
    word = random.choice(words)  # will choose a random word from the list of words in words.py
    while "-" in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

# function that hold the steps for playing hangman
def hangman():
    word = get_valid_word(words)  # variable that holds the result of the chosen word from the list
    word_letters = set(word)  # creates a set of letters from the random chosen word
    alphabet = set(string.ascii_uppercase)  # creates a set of uppercase letters from the alphabet to choose from
    used_letters = set()  # an empty set used to keep track of what the user has guessed

    lives = 6

    # getting user input and placing logic in while loop to keep iterating
    while len(word_letters) > 0 and lives > 0:

        # let user know what letters they have used
        print("You have used these letters: ", ' '.join(used_letters))  # It will join the used letters to the string

        # print what the users current word is based on used letters that user has guessed else print a - for each letter in word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()  # user input to guess a letter
        if user_letter in alphabet - used_letters:  # if the user input is in the alphabet minus the letters the user has guessed
            used_letters.add(user_letter)  # Then add the user letter to the set of used letters
            if user_letter in word_letters:  # if the user input is in the set of letters for the word
                word_letters.remove(user_letter)  # Then remove the letter from the user input

            else:
                lives = lives - 1
                print(f"Letter is not in word, you have {lives} lives left")

        elif user_letter in used_letters:  # if the user input guess is already in the set of used letters
            print("You have already used that letter. Please try again.")

        else:
            print("Invalid letter, please try again.")

    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("You guessed the word", word, "!!")


hangman()

