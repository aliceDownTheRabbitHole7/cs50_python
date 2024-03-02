def main():

    # Get user input

    text = input('Input: ')

    # Use function to convert input into emojis

    updated_text = convert(text)

    # Print the updated input to the console

    print(updated_text)

def convert(str):

    # Replace :) and :( with emojis

    message = str.replace(':)', '🙂').replace(':(', '🙁')
    return message

main()