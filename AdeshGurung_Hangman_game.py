
# This is a python script made by Adesh Gurung with the purpose of creating a hangman game for a Rockborne project submission.

# The general outline should be as follows:

# Print Welcome to the game, and then the rules of the game; the objective, the number of attempts

import random

# Step 1: Create a global list of words that will be used.

potential_words = ["turkey", "horse", "albania", "ford", "screen"]


# Step 2: Create functions that will select a word, mask a word, update masks based on successful guesses.

# A function that randomly selects a word, from a potential list of words.
def select_word():
    # choose random word from potential_words
    chosen_word = random.choice(potential_words)
    # convert to lowercase & return said word
    return(chosen_word.lower())
    
# A function that takes the chosen_word and masks the letters with underscores.
def mask_word(chosen_word):
    # Create a variable for the masked word
    masked = []

    # Count the length of the word
    length_of_word = len(chosen_word)

    #Based off the length of the word, how many _ will we have?
    for n in range(length_of_word):
        masked.append("_")
    
    return masked

# A function that will update the masked word, based on successful guesses of letters.
def update_pattern(chosen_word, masked, guess):
    
    # Go through the index of the chosen word
    for index in range(len(chosen_word)): # Using the range we determine how many times to loop this part
        if chosen_word[index] == guess: # when the letter associated with the index is equal to the guess
            masked[index] = guess # we update the mask with the guessed letter
    
    return masked


# Step 3: Game functionality, asking for player input!

guess = input("Please make a guess: ").lower() # Standardise everything to lowercase

# We need a function that checks if the guess is valid, it should return true or false to test the guess.
def valid_guess(guess, secret_word):
    
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
    if len(guess) == len(secret_word):
        return True

    # Otherwise invalid
    return False


# Step 4: Variable set up

# We have the functions, now we need to utilise them to generate variables for the game.

secret_word = select_word()
masked = mask_word(secret_word)
attempts = 5
guess_count = 0

# Step 5: The main game mechanic

# What do I need to do here is ... set up the main loop logic, which is while there are attempts, keep asking for input

# Using a while loop, because I want the game to run, given a condition is true
while attempts > 0 and "_" in masked:
    print(" ".join(masked))
    print(f"Attempts left: {attempts}")
    guess = input("Please make a guess: ").lower()

    # Lets check that the input is valid
    if not valid_guess(guess, secret_word):
        print("Invalid input!")
        continue

    if len(guess) == 1:
        #This is a branching point, distinguishing if we have a single letter guess.
        if guess in secret_word:
            update_pattern(secret_word, masked, guess)
        else:
            attempts -= 1

    if len(guess) == len(secret_word):
        #This is the instance of a whole word guess
        if guess == secret_word:
            print("Correct Guess! You have won!")
            break # End the loop, because you won
        else:
            attempts -= 1


# If one of the two conditions are not met in the main loop above, the code will run and a check will occur:

# Did the loop not start because all the letters in the masked word were guessed?
if "_" not in masked:
    print("Congratulations! Word is guessed")
else:
    print(f"You lost! The word was: {secret_word}")


    