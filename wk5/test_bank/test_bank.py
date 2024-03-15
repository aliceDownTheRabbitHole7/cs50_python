import pytest
from .bank import response

def main():
    test_hello()
    test_h()
    test_number()
    test_none()

# Check to see if the function returns '$0' if the greeting began with 'Hello'

def test_hello():
    assert response('Hello, Alek!') == '$0'
    assert response('Hello! How are you?') == '$0'
    assert response('Hello, world!') == '$0'

# Check to see if the function returns '$20' if the greeting began with 'H'

def test_h():
    assert response('Hi there, buddy!') == '$20'
    assert response('Hey there!') == '$20'
    assert response('Howdy, partner.') == '$20'

# Check to see if the function returns '$100' if the greeting does not start with either an 'H' or 'Hello'

def test_none():
    assert response('Welcome!') == '$100'
    assert response('Salutations!') == '$100'
    assert response('Please, come in.') == '$100'

# Check to see if the function raises an error if the input was a number

def test_number():
    with pytest.raises(AttributeError):
        response(777)
        response(3.1415926535897)
        response(9876543210)

if __name__ == '__main__':
    main()