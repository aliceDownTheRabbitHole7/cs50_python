import sys as s
from pyfiglet import Figlet

figlet = Figlet()

# If the amount of arguments given in the command line is equal to 1, then the program will pick a random font

if len(s.argv) == 1:
    random_font = True

# If the amount of arguments given in the command line is equal to 3 the program will use the font you choose
    
elif len(s.argv) == 3 and (s.argv[1] == '-f' or s.argv[1] == '--font'):
    random_font = False

# If neither of the above is true then exit the program

else:
    print('Invalid usage')
    s.exit(1)


# Get user input

text = input('Text: ')

# If the user chose a font, set the text to that font and render it to the console if possible, otherwise exit

if random_font == False:
    try:
        figlet.setFont(font=s.argv[2])
        print(figlet.renderText(text))
    except:
        print('Invalid usage')

# Otherwise render the default font

else:
    print(figlet.renderText(text))


