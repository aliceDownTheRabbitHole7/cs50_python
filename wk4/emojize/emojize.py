import emoji as e

# Get user input

input = input('Code: ')

# Convert it to emoji if possible and return it to the console

print(f'Output: {e.emojize(input)}')