import sys

# Iterate through lines in file and count how many lines have code (not including comments or white space)

def main():
    check_argv()

    try:
        file = open(sys.argv[1], 'r')
        lines = file.readlines()
    except FileNotFoundError:
        sys.exit()

    line_count = 0
    for line in lines:
        if check_lines(line) == False:
            line_count += 1
        else:
            pass
        
    print(line_count)

# Checks to ensure there are the correct amount of command-line arguments and that they are the proper extension

def check_argv():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments.')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments.')
    elif '.py' not in sys.argv[1]:
        sys.exit('Not a Python file.')

# Check to see if the current line in the file is a comment or white space

def check_lines(line):
    if line.isspace():
        return True
    elif line.lstrip().startswith('#'):
        return True
    else: 
        return False

if __name__ == '__main__':
    main()