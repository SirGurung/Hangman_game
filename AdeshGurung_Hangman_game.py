"""
Hangman Game - Project Submission by Adesh Gurung

This module implements a simple text-based Hangman game. It includes
functions to select a random word, create a masked pattern, update the
pattern based on player guesses, and validate input. The main loop handles
attempt tracking, win/loss detection, and replay logic.

"""

# ----------------
# Library / Package imports
# ----------------

import random

# ----------------
# List of potential words
# ----------------

potential_words = ["turkey", "horse", "albania", "ford", "screen"]


# ----------------
# Function defintions
# ----------------

def select_word():
    """
    Select and return a random word from the available list of potential_words

    returns:
        str: a randomly chosen word, in lowercase, just for standardisation reasons 
    
    """
    chosen_word = random.choice(potential_words)
    # convert to lowercase & return said word
    return(chosen_word.lower())
    

def mask_word(chosen_word):
    """
    A function that takes the chosen_word and masks the letters with underscores.

    Each letter is replaced with an underscore, this creates a sort of mask of the chosen word.
    Allowing the player to be able to start guessing what the word is, and what letters are missing

    Arg:
        chosen_word: so this was the randomly chosen word that the select_word function returns

    returns:
        list: a list of underscores that represents the hidden letters

    """
    masked = []

    # Count the length of the word
    length_of_word = len(chosen_word)

    #Based off the length of the word, how many _ will we have?
    for n in range(length_of_word):
        masked.append("_")
    
    return masked


def update_pattern(chosen_word, masked, guess):
    """ 
    A function that will reveal positions of a correctly guessed letter in the masked pattern.

    This function goes through the chosen word, and will update the masked pattern whenever the
    guess matches the letter that is in the position

    args:
        chosen_word: the full word that is being guessed
        masked_word: the current masked pattern that represents revealed and hidden letters

    returns:
        list: the updated masked pattern after any successful matches
    
    """
    # Go through the index of the chosen word
    for index in range(len(chosen_word)): # Using the range we determine how many times to loop this part
        if chosen_word[index] == guess: # when the letter associated with the index is equal to the guess
            masked[index] = guess # we update the mask with the guessed letter
    
    return masked




# We need a function that checks if the guess is valid, it should return true or false to test the guess.
def valid_guess(guess, chosen_word):
    """ 
    This function will validate the player's guess input

    I do this because I do not want to accept invalid inputs, such as:
    1. Non alphabetical characters; @!-7 etc
    2. It should be a one letter guess or the whole word, nothing else!

    args:
        guess: this is the single letter or word, that the player will guess upon being prompted
        chosen_Word: This is the secret word, used for length comparisons
    
    retunrs:
        boolean: this function checks if a condition is true or false, and returns either one
    """
    # Must not be empty
    if len(guess) == 0:
        return False
    
    # Must contain only letters
    if not guess.isalpha():
        return False

    # Single letter guess is valid
    if len(guess) == 1:
        return True

    # Full-word guess matching secret_word length is valid
    if len(guess) == len(chosen_word):
        return True

    # Otherwise invalid
    return False


# ----------------
# Main game loop
# ----------------

# Global Statistics
total_games = 0
wins = 0
losses = 0

# Initiate the play loop by setting the default of wants_to_play to yes
wants_to_play = "y"


while wants_to_play == "y":
# Setting up a single round
    attempts = 5
    guess_count = 0
    chosen_word = select_word()
    masked = mask_word(chosen_word)
    wrong_letters = []
    round_won = False
    user_quit = False
    print("Welcome to Hangman! Your goal is to guess the word correctly within 5 attempts.")
    print("You may input a single letter or full word guess!")
    print("If you wish to quit the game input quit or exit")

    # Main game logic loop 
    while attempts > 0 and "_" in masked:
        print(" ".join(masked))
        print(f"Attempts left: {attempts}")
        guess = input("Please make a guess: ").lower()

        # I want to add the option to quit the game midway
        if guess in ["quit","exit"]:
            user_quit = True
            break

        # Lets check that the input is valid
        if not valid_guess(guess, chosen_word):
            print("Invalid input!")
            continue

        guess_count += 1

        if len(guess) == 1:
            #This is a branching point, distinguishing if we have a single letter guess.
            if guess in chosen_word:
                update_pattern(chosen_word, masked, guess)
            else:
                attempts -= 1

        if len(guess) == len(chosen_word):
            #This is the instance of a whole word guess
            if guess == chosen_word:
                round_won = True
                print("Correct Guess! You have won!")
                break # End the loop, because you won
            else:
                attempts -= 1

    # Round finished
    if user_quit:
        print("Game ended early")
        break # if they want to quit, no need to continue running the code

    total_games += 1

    if "_" not in masked:
        round_won = True

    if round_won:
        wins += 1
        print("Congratulations!")
    else:
        losses += 1
        print(f"You lost! The word was: {chosen_word}")

    # Play again
    ans = input("Play again? (y/n): ").strip().lower()
    if not ans.startswith("y"):
        break

# Print statistics after loop ends
print(f"Total games: {total_games}")
print(f"Wins: {wins}")
print(f"Losses: {losses}")





    