import random as r

# Choose the maximum range

while True:
    try:
        n = int(input('Level: '))
        if (n < 0):
            print('Choose a positive integer.')
        else:
            break
    except:
        print('Choose a positive integer.')

# Randomly select the target number

number = r.randint(0, n)

# The user guesses until they are correct

while True:
    try:
        guess = int(input('Guess: '))
        if (guess < 0):
            print('Choose a positive integer.')
        elif (guess > number):
            print('Too large!')
        elif (guess < number):
            print('Too small!')
        else:
            print('Just right!')
            break
    except ValueError:
        print('Choose a positive integer.')



