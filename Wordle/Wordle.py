import random


def read_words(x):
    """function reads in words and assigns it to variable 'Possible Words'"""
    with open(x, encoding='utf8', newline='') as word_data:
        possible_words = []
        for line in word_data:
            possible_words.append(line.rstrip())

    return possible_words


def guess_check(users_guess, answer):
    if guess == chosen_word:
        return True

    else:
        for position, letter in enumerate(users_guess):
            if users_guess[position] == chosen_word[position]:
                print("\033[32m" + users_guess[position] + "\033[0m", end='')

            elif users_guess[position] in chosen_word:
                print("\033[33m" + users_guess[position] + "\033[0m", end='')
            else:
                print(users_guess[position], end='')

        print()


filename = 'WordCatalogue.txt'
word_list = read_words(filename)
number_of_guesses = 0

chosen_word = word_list[random.randint(1, len(word_list))]


print('Welcome to wordle')
print("*" * 70)

print('Please guess a word between with 5 characters: ')

while True:
    guess = input().casefold()

    if len(guess) == 5:
        if guess_check(guess, chosen_word):
            print('You have guessed it correctly')
    else:
        print('Please ensure you enter a word containing five Letters')

    number_of_guesses += 1

    if number_of_guesses > 5:
        print(chosen_word)
        print('You have lost!')








