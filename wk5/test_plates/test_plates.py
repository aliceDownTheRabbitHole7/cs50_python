from .plates import is_valid

def main():
    test_first_chars()
    test_length()
    test_numbers()
    test_special()
    test_zero()

# Test to see if plate is between 2 and 6 characters

def test_length():
    assert is_valid('Tint97') == True
    assert is_valid('AB12') == True
    assert is_valid('California2012') == None
    assert is_valid('A') == None

# Test to see if the first 2 characters are letters
    
def test_first_chars():
    assert is_valid('Bear50') == True
    assert is_valid('Help11') == True
    assert is_valid('713She') == None
    assert is_valid('A91874') == None

# Test to see if numbers come at the end of the plate
    
def test_numbers():
    assert is_valid('Also21') == True
    assert is_valid('43Temp') == None
    assert is_valid('Hi33Me') == False
    assert is_valid('Na3124') == True

# Test to see if the first number is not a zero
    
def test_zero():
    assert is_valid('Melt01') == False
    assert is_valid('Tiny20') == True
    assert is_valid('Au0290') == False
    assert is_valid('Fe9701') == True

# Test to see if none of the characters are special characters
    
def test_special():
    assert is_valid('Mash12') == True
    assert is_valid('Tim708') == True
    assert is_valid('Wet!90') == None
    assert is_valid('Li.fe6') == None


if __name__ == '__main__':
    main()