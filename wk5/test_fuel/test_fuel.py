from .fuel import gauge, convert
import pytest

def main():
    test_zero()
    test_percent()
    test_gauge()

# Test the 'Divide by Zero' error

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert('10/0')
        convert('0/0')
        convert('-3/0')

# Test to see if the function converts the fraction into percent

def test_percent():
    assert convert('5/10') == 50
    assert convert('1/100') == 1
    assert round(convert('3/9'), 0) == 33

# Test to see if the guage function returns empty or full depending on the percentage passed through it

def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    
if __name__ == '__main__':
    main()



