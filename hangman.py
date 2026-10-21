#======================================#
#    Welcome to the hangman game 
#======================================#

import random
def play_hangman():
    words = ["python","computer","programming","developer","keyword"]

    secret_word = random.choice(words)
    guessed_letters = []
    attempts_left = 6

    print("=" * 35)
    print("   welcome to hangam!")
    print("guess the hidden word one letter at a time.")
    print("you have 6 incorrect guesses available.")

    while attempts_left>0:
        display_word = " ".join(
            letter if letter in guessed_letters else"_"
            for letter in secret_word
        )

        print("\nword:",display_word)
        print("incorrect guesses left:", attempts_left)

        if all(letter in guessed_letters for letter in secret_word):
            print("\ncongratulations! you guessed the world:", secret_word)
            print("you win!")
            break

        guess = input("enter a letter:").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
             print("Please enter a single alphabet letter.")
             continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            attempts_left -= 1
            print("Wrong guess!")

    else:
        print("\nGame over! You ran out of attempts.")
        print("The correct word was:", secret_word)

    print("\nThanks for playing Hangman!")


if __name__ == "__main__":
     play_hangman()
        
        
               

