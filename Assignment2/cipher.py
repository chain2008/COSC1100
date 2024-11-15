"""Module providing a function for Base 3 cipher."""
import random

# ASCII A is represented by the ASCII value 65.
ASCII_A = 64
BASE = 3
LENGTH = 3

def base3_cipher(letter, key):
    # Convert the letter to its corresponding ASCII code.
    ascii_code = ord(letter.upper()) - ASCII_A
    #ascii_code = ord(letter.upper()) - ASCII_A
    if ascii_code < 0 or ascii_code >= 26:
        return letter
    # Convert the ASCII code to base 3 and store digits in a list.
    digit_list = decimal_base(ascii_code, BASE)

    # Add leading zeros (if necessary) to make it 3 digits long.
    padding(digit_list,LENGTH,0)

    # Shuffle the first and nth digits by swapping the values in the list.
    # Note that key is a parameter to this function.
    hold_value = digit_list[key]
    digit_list[key] = digit_list[0]
    digit_list[0] = hold_value

    decimal_value = base_decimal(BASE,digit_list)

    # Return the output as a single letter.
    ret = chr(decimal_value + ASCII_A)
    #ret = chr(decimal_value + ASCII_A)
    return ret

def gen_key(length):
    key = [0] * length
    for index in range(0, length):
        key[index] = random.randint(0, 2)
    return key

def decimal_base(number,base):
    """convert decimal number into base digit_list
    example: decimal(5,3) return [1,2]
    """
    digit_list = []
    while number > 0:
        # Get the remainder from dividing the code by 3.
        remainder = number % base
        # This remainder becomes the first digit of the numeric value.
        digit_list.insert(0, remainder)
        # Force integer division.
        number = number // base
    return digit_list

def base_decimal(base, digit_list):
    """convert base digit_list to decimal
    example: base_decimal(3,[1,2]) return 5
    """
    decimal_value = 0
    # Now decode from ASCII which will result in an encoded letter.
    decimal_value = digit_list[0] * \
        (base * base) + digit_list[1] * (base) + digit_list[2]
    return decimal_value

def padding(digit_list, length, location = -1):
    """padding digiit_list with 0 to length
    location: 0 padding at front, -1 padding at end
    example: padding([1,2],3) return [0,1,2]
    """
    if location == 0:
        while len(digit_list) < LENGTH:
            digit_list.insert(0, 0)
    else:
        while len(digit_list) < LENGTH:
            digit_list.append(0)
