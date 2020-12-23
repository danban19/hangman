import random
import sys


def greetings():
    print("H A N G M A N")
    action = input('Type "play" to play the game, "exit" to quit: \n')
    if action == 'play':
        hangman_game()
    elif action == 'exit':
        sys.exit()
    else:
        greetings()


def hangman_game():
    words = ['python', 'java', 'kotlin', 'javascript']  # list of words to guess
    chosen_word = random.choice(words)  # random word chosen to guess
    attempts = 8
    guessed_letters = ''
    guess = list("-" * len(chosen_word))
    while attempts > 0:  # loop breaks after 8 attempts
        print('\n')
        print("".join(guess))
        letter = input('Input a letter: \n')
        if len(letter) != 1:  # checks if the guess is a single letter
            print("You should input a single letter\n")
            continue
        elif letter not in 'abcdefghijklmnopqrstuvwxyz':  # checks if the guess is a lowercase English letter
            print("Please enter a lowercase English letter\n")
            continue
        elif letter in chosen_word:
            if letter not in guess:  # letter in guess and not guessed before
                for i, element in enumerate(chosen_word):
                    if element == letter:
                        guess[i] = letter
            else:   # letter in guess and guessed before
                print("You've already guessed this letter")
        else:
            if letter in guessed_letters:
                print("You've already guessed this letter")
            else:
                print("That letter doesn't appear in the word")
                attempts -= 1
        if "".join(guess) == chosen_word:  # checks if the user guessed the word
            print("You guessed the word!")
            print("You survived!")
            sys.exit()
    print("You lost!")  # fail if all the attempts are used


greetings()
