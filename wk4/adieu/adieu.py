import inflect

inf = inflect.engine()

# Init empty list of names

names = []

# Ask user for names to add to the list of names

while True:
    try:
        name = input('Name: ')
        names.append(name)

    # Break out of the loop with 'ctrl + c'

    except KeyboardInterrupt:
        print()
        break

# Print a farewell to the list of people the user gave

print(f'Adieu, adieu, to {inf.join(names)}')