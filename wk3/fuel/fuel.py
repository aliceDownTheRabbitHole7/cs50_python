# Get fraction from user and store numerator and denominator into variables
while True:
    try:
        fraction = input('Fraction: ').split('/')
        x = int(fraction[0])
        y = int(fraction[1])

        # Turn the fraction into a percent

        percent = x/y*100
        if x/y <= 1:
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

# Print percent to console, then if the tank is less than 1% or greater than 99% it will print E or F respectively

print(f'{percent:.0f}%', end=' ')

if percent >= 99:
    print('F')
elif percent <= 1:
    print('E')
