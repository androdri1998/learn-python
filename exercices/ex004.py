value = input('Type anything: ')

type_value = type(value)
is_alnum = value.isalnum()
is_alpha = value.isalpha()
is_decimal = value.isdecimal()
is_digit = value.isdigit()
is_identifier = value.isidentifier()
is_lower = value.islower()
is_numeric = value.isnumeric()
is_printable = value.isprintable()
is_space = value.isspace()
is_title = value.istitle()
is_upper = value.isupper()

print()
print('Description about value typed')
print()
print("type: {}".format(type_value))
print("It's an alphanumeric: {}".format(is_alnum))
print("It's an alphabetic: {}".format(is_alpha))
print("It's a decimal: {}".format(is_decimal))
print("It's a digit: {}".format(is_digit))
print("It's an identifier: {}".format(is_identifier))
print("It's all lower letter: {}".format(is_lower))
print("It's a numeric: {}".format(is_numeric))
print("It's a printable: {}".format(is_printable))
print("It's a space: {}".format(is_space))
print("It's a title: {}".format(is_title))
print("It's all upper letter: {}".format(is_upper))