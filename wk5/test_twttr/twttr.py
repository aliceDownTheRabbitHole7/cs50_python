# Get user input, pass it through a shortening function, and print the result to the console

def main():
    text = input('Input: ')
    print(f'Output: {shorten(text)}')

# Iterate through input and remove lowercase vowels

def shorten(word):
    for letter in word:
        if letter in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
            word = word.replace(letter, '')
        else:
            pass
    return word


if __name__ == "__main__":
    main()