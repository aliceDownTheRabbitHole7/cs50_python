def main():
    while True:
        try:
            fraction = input('Fraction: ')
            split_fraction = fraction.split('/')
            if (int(split_fraction[0]) <= int(split_fraction[1]) and int(split_fraction[0]) >= 0) and int(split_fraction[1]) > 0:
                break
        except ValueError:
            pass
    percentage = convert(fraction)
    reading = gauge(percentage)
    print(f'{percentage:.0f}%')
    print(reading)

# Convert inputted fraction into a percent
    
def convert(fraction):
    new_fraction = fraction.split('/')
    x = int(new_fraction[0])
    y = int(new_fraction[1])
    percent = x/y*100
    if percent <= 100:
        return percent

# Pass the percentage through a function to see if the tank is empty or full
        
def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'

if __name__ == '__main__':
    main()