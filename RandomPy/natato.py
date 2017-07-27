import random

cities = ["Istanbul", "Ankara", "Konya", "Malatya"]

def chooseword():
    return random.choice(cities)

lives_remaining = 14

guessed_letters = ""

def play():
    word = chooseword()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print "Congratulations, human. You have defeated me."
            break
        if lives_remaining == 0:
            print "You can never beat me, human."
            print "My city was:" + " " + word
            break

def get_guess(word):
    print_word_with_blanks(word)
    print "Lives remaining:" + " " + str(lives_remaining)
    guess = (raw_input("Guess a letter or the whole city!").lower())
    return guess

def print_word_with_blanks(word):
    display_word = ""
    for letter in word:
        if guessed_letters.find(letter) > -1:
            display_word = display_word + letter
        else:
            display_word = display_word + "-"
    print display_word

def process_guess(guess, word):
    if len(guess) > 1:
        return whole_word_guess(guess, word)
    else:
        return single_letter_guess(guess, word)

def single_letter_guess(guess, word):
    global guessed_letters
    global lives_remaining
    if word.find(guess) == -1:
        lives_remaining -= 1
    guessed_letters += guess
    if all_letters_guessed(word):
        return True

def all_letters_guessed(word):
    for letter in word:
        if guessed_letters.find(letter) == -1:
            return False
    return True

def whole_word_guess(guess, word):
    global lives_remaining
    if guess.lower() == word.lower():
        return True
    else:
        lives_remaining -= 1
        return False
play()
