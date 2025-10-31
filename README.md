# Hangman_game

# This README explains:
- The purpose of the project
- How it works
- How to run and interact wtih the game
- Its features and internal structure

## Game description
A simple text-based Hangman game written in Python. Players must guess a randomly selected secret word within a limited number of attempts. The word is displayed in a masked form using underscores (e.g. `hello` -> `_ _ _ _ _`). The game provides clear instructions, validates input, and prevents unexpected crashes. Players may guess a single letter or attempt the full word at any time. An option to exit the game mid-round is also included.

## How to run

1. Install code editor such as VScode, and download Python package.
2. Download this repository (Codwe -> Download ZIP).
3. Open the hangman_game.py file in the code editor.
4. Run the game in the code editor terminal with "python AdeshGurung_Hangman_game.py"

## How to play the game
The game displays the hidden word as underscores.

Guess one letter at a time to reveal matching letters.

Alternatively, you can attempt to guess the full word.

Incorrect guesses reduce your remaining attempts.

When all letters are revealed, you win the round.

When attempts reach zero, the round ends in a loss.

Type quit at any time to stop the current game.

## Code features
- Randomly selected secret words from a word bank
- Input validation (letters only, guesses must be one letter or the length of the secret word)
- Tracks total games played, wins and losses and displays game statistics
- Option to exit mid-game safely
- Invalid inputs do not consume attempts
- The option to play again

## Program structure
The game uses several functions to remain modular and easy to maintain.

select_word() – randomly selects the secret word
mask_word() – generates the initial masked pattern
update_pattern() – reveals correctly guessed letters
valid_guess() – ensures the user input is acceptable

The main game uses while loops, to check if the player has attempts left, else the loop is exited and the game is terminated.

## Tracked statistics
At the end of each round, the following are updated:
- The total games played
- Number of wins
- Number of losses
- Remaining attempts

  
