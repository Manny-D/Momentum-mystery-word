import random

def play_game():
    with open('words.txt') as f:
        word_string = f.read()
        word_list = word_string.split()
        current_word = random.choice(word_list)
        
    # Made function to be reused later
    def play_again():  
        interested = input("\nGreetings Professor Falken.\nShall we play a game? (y/n) \n")
        if interested.lower() == "y":
            print("Ok.. let's play!\n" "Your word is", len(current_word), "letters long.")
        elif interested.lower() == "n":
            print("A strange game.\nThe only winning move is not to play.\nHow about a nice game of chess?")
            exit()
        else:
            print("Invalid input. Try again.")
            play_game()

    play_again()

# The Game
    answer = []
    count = 8

    while True:
        w = 0
        guess = input("\nPlease enter 1 letter as your guess: ")

        # Invalid input handling
        # If input is a number:
        if not guess.isalpha(): # looks to be working now
            print("\nInvalid entry: " + guess + ". Please enter a letter only.")
        # If input is multiple characters:    
        elif len(guess) > 1:   # looks to be working even if correct letter entered
            print("\nInvalid entry: " + guess + ". Only 1 letter please.")

        # Guess logic
        elif guess in answer: 
            print("\nYou already tried that letter.\nYou have " + str(count) + " guesses remaining.")
        elif guess in current_word:
            print("\nYou got one!\nYou have " + str(count) + " guesses remaining.")
            answer += guess
        else:
            count -= 1
            answer += guess
            print("\nSorry no " + guess + "'s try again!\nYou have " + str(count) + " guesses remaining.")

        # Ends game when count is 0 - this logic feels off, but works  ¯\_(ツ)_/¯ 
        if count == 0:
            print("\nGame Over!!\nNo more guesses left =(\nThe Mystery Word was " + current_word + ".")
            play_again()
        
        # Loop: letters - aka. char and hidden - aka _'s
        for char in current_word:
            if char in answer:
                print(char, end = "")
            else:
                print("_", end = "")
                w += 1

        if w == 0: # Working - tries removed though
            print("\nYou did it!\nThe Mystery Word was " + current_word + "!")
            play_again()

        # if w == 0: # working but count is off / want to try something different
        #     print("\nYou did it!\nThe Mystery Word was " + current_word + " and was solved in " + str(tries) + " guesses!")
        #     exit()

if __name__ == "__main__":
    play_game()