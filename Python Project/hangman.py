import random
from collections import Counter

some_words = '''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

some_words = some_words.split(' ')
word = random.choice(some_words)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    for i in word:
        print('_', end=' ')
    print()

    playing = True
    letter_guessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0

    try:
        while chances != 0 and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            # Validation of the guess
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letter_guessed:
                print('You have already guessed that letter')
                continue

            # If letter is guessed correctly
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letter_guessed += guess  # Add guess as many times as it occurs

            # Print the word
            for char in word:
                if char in letter_guessed and Counter(letter_guessed) != Counter(word):
                    print(char, end=' ')
                    correct += 1
                # User guessed all letters
                elif Counter(letter_guessed) == Counter(word):
                    print("The word is: ", word)
                    flag = 1
                    print('Congratulations, You won!')
                    break  # Exit both loops
                else:
                    print('_', end=' ')

            # User used all chances
            if chances <= 0 and Counter(letter_guessed) != Counter(word):
                print()
                print('You lost! Try again..')
                print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()