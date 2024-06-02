def roman_to_integer(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0

    for i in range(len(roman)):
        if i > 0 and roman_numerals[roman[i]] > roman_numerals[roman[i - 1]]:
            integer_value += roman_numerals[roman[i]] - 2 * roman_numerals[roman[i - 1]]
        else:
            integer_value += roman_numerals[roman[i]]

    return integer_value


# Example usage:
roman_numeral = input("Enter a Roman numeral: ")
print("Integer value:", roman_to_integer(roman_numeral))

# OR

print("*"*100)

def roman_to_integer(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    prev_value = 0

    for numeral in roman[::-1]:
        value = roman_numerals[numeral]
        if value < prev_value:
            integer -= value
        else:
            integer += value
        prev_value = value

    return integer


# Example usage:
roman_numeral = input("Enter a Roman numeral: ")
print("Integer:", roman_to_integer(roman_numeral))

