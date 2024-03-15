def main():

    # Get user input and convert it to lowercase then pass it through the response function

    greeting = input('Greeting: ')
    reward = response(greeting)
    print(reward)


# Check conditional to see if 'Hello' or 'H' is at the beginning of the greeting then return result

def response(word):
    if word.startswith('hello') or word.startswith('Hello'):
        return f'$0'
    elif word[0] in ['h', 'H'] :
        return f'$20'
    else:
        return f'$100'
    

if __name__ == '__main__':
    main()