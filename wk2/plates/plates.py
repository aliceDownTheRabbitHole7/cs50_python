def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Check to see if plate is between 2 and 6 characters, if the first 2 characters are letters, and if the text is all alpha/numeric

    if 6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum():

        # Iterate through the plate until there is a number. Then check to see if that number isn't 0 and if all the following characters are all numbers.

        for char in s:
            if char.isdigit():
                i = s.index(char)
                if s[i:].isdigit() and int(char) != 0:
                    return True
                else:
                    return False


main()