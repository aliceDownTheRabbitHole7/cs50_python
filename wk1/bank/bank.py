def main():

    # Get user input and convert it to lowercase

    greeting = input('Greeting: ').lower()

    # Check conditional to see if 'Hello' or 'H' is at the beginning of the greeting then print result to console

    if greeting.startswith('hello'):
        print('$0')
    elif greeting[0] == 'h':
        print('$20')
    else:
        print('$100')

main()