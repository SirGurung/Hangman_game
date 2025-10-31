
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
    secret_word = select_word()
    masked = mask_word(secret_word)
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
        if not valid_guess(guess, secret_word):
            print("Invalid input!")
            continue

        guess_count += 1

        if len(guess) == 1:
            #This is a branching point, distinguishing if we have a single letter guess.
            if guess in secret_word:
                update_pattern(secret_word, masked, guess)
            else:
                attempts -= 1

        if len(guess) == len(secret_word):
            #This is the instance of a whole word guess
            if guess == secret_word:
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
        print(f"You lost! The word was: {secret_word}")

    # Play again
    ans = input("Play again? (y/n): ").strip().lower()
    if not ans.startswith("y"):
        break

# Print statistics after loop ends
print(f"Total games: {total_games}")
print(f"Wins: {wins}")
print(f"Losses: {losses}")





    