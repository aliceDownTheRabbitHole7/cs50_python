import pytest
from .twttr import shorten

def main():
    test_lower()
    test_upper()
    test_number()

# Test to see if the funtion removes lowercase vowels

def test_lower():
    assert shorten('wukong') == 'wkng'
    assert shorten('hello, world!') == 'hll, wrld!'
    assert shorten('aleksander white') == 'lksndr wht'

# Test to see if the funtion removes uppercase vowels

def test_upper():
    assert shorten('WHY SO SERIOUS?') == 'WHY S SRS?'
    assert shorten('GITHUB') == 'GTHB' 
    assert shorten('FACEBOOK') == 'FCBK' 

# Test to see if a numeric input raises an error
    
def test_number():
    with pytest.raises(TypeError):
        shorten(3.14)
        shorten(50)
        shorten(1234567890)

if __name__ == '__main__':
    main()

