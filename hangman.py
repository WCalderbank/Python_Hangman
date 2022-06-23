from curses.ascii import isalpha
import random
from words import random_word

def get_word():
    word = random.choice(random_word)
    return word.upper()

def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Lets Play A Game!")
    print(tries)
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please Guess A Letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You Have Already Used This Letter", guess)
            elif guess not in word:
                print(guess, "Is Not in The Word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Nice Guess,", guess, "Is Correct!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You Already Guessed That", guess)
            elif guess != word:
                print(guess, "Is Not The Word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        
        else:
            print("Not A Valid Guess, Try Again")
        print(tries)
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, You Guessed The Correct Word! You Win !")
    else:
        print("Sorry You Ran Out Of Tries, The Word Was... " + word)


def main():
    word = get_word()
    play(word)
    while input("Wanna Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
