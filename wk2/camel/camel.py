# Get user input

camel = input('camelCase: ')

# Set up response

print('snake_case: ', end='')

# Iterate through user input and insert underscores and remove capitalizations

for letter in camel:
    if letter.isupper():
        print('_' + letter.lower(), end='')
    else:
        print(letter, end='')


