# Get user input, pass it through a shortening function, and printing the result to the console

def main():
    text = input('Input: ')
    shortened = shorten(text)
    print(f'Output: {shortened}')

# Iterate through input and remove lowercase vowels

def shorten(word):
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            word = word.replace(letter, '')
        else:
            pass
    return word


if __name__ == "__main__":
    main()