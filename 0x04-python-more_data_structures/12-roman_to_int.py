#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_dict = {
            'T': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }
    integer_value = 0
    prev_value = 0

    for symbol in roman_string[::-1]:
        value =  roman_dict.get(symbol, 0)
        if value < prev_value:
            integer_value -= value
        else:
            integer_value += value
        prev_value = value
    return integer_value
