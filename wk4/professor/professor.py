import random

def main():
    level = get_level()
    score = game(level)
    print(f'Score: {score}')


# Request input until user chooses a level between 1 and 3

def get_level():
    while True:
        try:
            n = int(input('Level: '))
            if n > 0 and n <= 3:
                break
        except ValueError:
            pass
    
    return n

# Choose the difficulty depending on the level the user chose

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

# Continue to ask the user for the answer until they are correct or guess incorrectly 3 times

def attempts(x, y):
    round = 1
    while round <= 3:
        try:
            answer = int(input(f'{x} + {y} = '))
            if answer == x + y:
                return True
            else:
                round += 1
                print('EEE')
        except ValueError:
            round += 1
            print('EEE')
    print(f'x + y = {x + y}')

# Generate 10 math problems and keep score of how many correct answers were given

def game(level):
    counter = 1
    score = 0
    while counter <= 10:
        x, y = generate_integer(level)
        answer = attempts(x, y)
        if answer == True:
            score +=1
        counter += 1
    return score



if __name__ == "__main__":
    main()