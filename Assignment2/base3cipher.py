"""Module providing a function for Base 3 cipher."""
import random

# ASCII A is represented by the ASCII value 65.
ASCII_A = 65
BASE = 3
LENGTH = 3


def base3_cipher(letter, key):
    # Convert the letter to its corresponding ASCII code.
    ascii_code = ord(letter.upper()) - ASCII_A
    if ascii_code < 0 or ascii_code > 26:
        return letter
    # Convert the ASCII code to base 3 and store digits in a list.
    digit_list = []
    while ascii_code > 0:
        # Get the remainder from dividing the code by 3.
        remainder = ascii_code % BASE
        # This remainder becomes the first digit of the numeric value.
        digit_list.insert(0, remainder)
        # Force integer division.
        ascii_code = ascii_code // BASE

    # Add leading zeros (if necessary) to make it 3 digits long.
    while len(digit_list) < LENGTH:
        digit_list.insert(0, 0)

    # Shuffle the first and nth digits by swapping the values in the list.
    # Note that key is a parameter to this function.
    hold_value = digit_list[key]
    digit_list[key] = digit_list[0]
    digit_list[0] = hold_value

    decimal_value = 0
    # Now decode from ASCII which will result in an encoded letter.
    decimal_value = digit_list[0] * \
        (BASE * BASE) + digit_list[1] * (BASE) + digit_list[2]

    # Return the output as a single letter.
    ret = chr(decimal_value + ASCII_A )
    return ret

def gen_key(length):
    key = [0] * length
    for index in range(0, length):
        key[index] = random.randint(0, 2)
    return key
