import random

# Have user choose the maximum range to guess within

while True:
    n = int(input('Max range: '))
    if n > 0:
        break
        
# The program chooses a random number within that range

number = random.randint(1, n)

# Prompt the user to continue guessing until they guess correctly

while True:
    try:
        guess = int(input('Guess: '))
        if guess < number:
            print('Too small!')
        elif guess > number:
            print('Too large!')
        elif guess == number:
            print('Just right!')
            break
    except ValueError:
        pass