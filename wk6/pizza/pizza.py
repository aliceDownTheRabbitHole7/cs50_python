import sys
import csv
from tabulate import tabulate

def main():
    check_argv()
    data = []
    try:
        with open(sys.argv[1], 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        sys.exit("File not found.")
    print(tabulate(data[1:], headers=data[0]))

# Check to see if there are the correct quantity of command-line arguments and if the second argument is a CSV file

def check_argv():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments.')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments.')
    elif '.csv' not in sys.argv[1]:
        sys.exit('Not a CSV file.')

if __name__ == '__main__':
    main()