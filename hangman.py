import random
from words import words

def get_correct_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_correct_word(words)
    word_letters = set(word)