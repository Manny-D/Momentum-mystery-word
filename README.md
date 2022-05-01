# Mystery Word

## Objectives

After completing this assignment, you should be able to:

- Create an interactive program.
- Read from a file.
- Choose a random value.
- Keep track of state.

## Details

For this lab, you will implement a word-guessing game we call Mystery Word. In your game, the player plays against the computer. This game will run on the command-line as a text-only interactive game.

### Included files

#### `mystery_word.py`

This is a starter file. Delete the keyword `pass` in the `play_game` function and write your code from there. You do not have to change the code below the line that says `if __name__ == "__main__":`.

Notice that you are not passing in the file name as an argument on the command line. You should open the file yourself in your code, using its path.

#### `words.txt`

This is the source file your game will use to choose the secret word.

#### `test-word.txt`

This is a test file with only ONE word in it, instead of 58,000. It's a lot easier to think about one word while you're developing the game. You can change it if you want.


## Minimum Requirements

Your program should run when you run this file like this:

```py
python mystery_word.py
```

The computer (that's you, writing this in Python code) must select a word at random from the list of words in the file `words.txt`, provided in this repo. This becomes the secret word for the game.

### Game Flow

1. At the start of the game, let the user know how many letters the secret word contains.

2. Ask the user to supply one guess (i.e. letter) per round. This letter can be upper or lower case and it should not matter. If a user enters more than one letter, tell them the input is invalid and let them try again.

3. Let the user know if their guess appears in the secret word.

4. Display the partially guessed word, as well as letters that have not been guessed. For example, if the word is BOMBARD and the letters guessed are `a`, `b`, and `d`, the screen should display:

```txt
B _ _ B A _ D
```

### Game Rules

A user is allowed 8 guesses. Remind the user of how many guesses they have left after each round.

_A user loses a guess only when they guess incorrectly._ If they guess a letter that is in the secret word, they do not lose a guess.

If the user guesses the same letter twice, do not take away a guess.

Instead, print a message letting them know they've already guessed that letter and ask them to try again.

The game should end when the user constructs the full word or runs out of guesses.

If the player runs out of guesses, reveal the word to the user when the game ends.

### More features

Once the minimum requirements are in place, implement these features. You may not get to these, and that is ok!

1. Let the user choose a level of difficulty at the beginning of the game.
   Easy mode only has words of 4-6 characters; normal mode only has words of 6-8
   characters; hard mode only has words of 8+ characters.
2. When a game ends, ask the user if they want to play again. The game begins again with a new secret word if they reply positively.
3. Use pipenv to install the [colorama package](https://github.com/tartley/colorama) to add colors to your terminal output. If you want to get really fancy, check out [asciimatics](https://github.com/peterbrittain/asciimatics)!

## 🌶 Spicy Mode

Implement the [evil version of this game](http://nifty.stanford.edu/2011/schwarz-evil-hangman/).
Put it in a new Python program called "demon_words.py".

### Attribution

This lab is based off a similar exercise in MIT's 6.00.1x course.
