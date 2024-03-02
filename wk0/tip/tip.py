def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):

    # Convert string into a floating int

    d_float = float(d)
    return d_float

    # Convert percent to floating int

def percent_to_float(p):
    p_float = int(p)/100
    return p_float


main()