def main():

    # Get user input and convert it to lower case as well as strip outer white space

    text = input('What is the answer to the Great Question of life, the universe, and everything? ').lower().strip()

    # Check conditional to see if text is the correct answer and then print answer to console

    if text == 'forty two' or text == '42' or text == 'forty-two':
        print('Yes')
    else:
        print('No')

main()