def main():

    # Get user input

    mass = int(input('Mass(kg): '))

    # Pass the input through the conversion function

    energy = convert(mass)

    # Print output to console

    print(f'Energy = {energy}')

def convert(m):

    # Calculate E = mc^2

    e = m * (3000000 * 3000000)
    return e

main()