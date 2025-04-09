"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""
import doctest
from prac_06.car import Car

def repeat_string(s, n):
    return " ".join([s] * n)

def is_long_word(word, n=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= n

def format_sentence(phrase):
    """
    Format a phrase as a sentence with a capital start and single full stop.
    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('hi there')
    'Hi there.'
    """
    return phrase.rstrip('.').capitalize() + '.'

def run_tests():
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"
    car_default = Car()
    assert car_default.fuel == 0, "Car does not set default fuel correctly"
    car_specified = Car(fuel=10)
    assert car_specified.fuel == 10, "Car does not set specified fuel correctly"

run_tests()
doctest.testmod()