import random
print("H A N G M A N")
print("\n")
words = ['python', 'java', 'kotlin', 'javascript']
chosen_word = random.choice(words)
attempts = 8
guessed_letters = ''
guess = list("-" * len(chosen_word))
while attempts > 0:
    print("\n")
    print("".join(guess))
    letter = input("Input a letter:")
    if len(letter) != 1:
        print("You should input a single letter\n")
        continue
    if letter not in 'abcdefghijklmnopqrstuvwxyz':
        print("Please enter a lowercase English letter\n")
        continue
    if letter in chosen_word:
        if not letter in guess:
            for i, element in enumerate(chosen_word):
                if element == letter:
                    guess[i] = letter
        else:
            print("You've already guessed this letter")
    else:
        if letter in guessed_letters:
            print("You've already guessed this letter")
        else:
            print("That letter doesn't appear in the word")
            attempts -= 1
    if "".join(guess) == chosen_word:
        print("You guessed the word!")
        print("You survived!")
        break
    guessed_letters += letter
else:
    print("You lost!")
