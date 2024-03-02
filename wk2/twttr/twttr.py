# Vowel bank

vowels = ['a', 'e', 'i', 'o', 'u']

# Get user input

text = input('Input: ')

print('Output: ', end='')

# Iterate through the input and remove the vowels

for letter in text:
    if letter in vowels:
        text = text.replace(letter, '')
    else:
        pass

# Print result to the console

print(text)

