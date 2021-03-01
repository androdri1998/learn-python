random_number = int(input("Type a number: "))
print("- 1 for binary")
print("- 2 for octal")
print("- 3 for hexadecimal")
binary_base = int(input("What's the binary base to covert? type a correspondent number: "))

binary = 1
octal = 2
hexadecimal = 3

full_name_base_numbers = [
    "Binary",
    "Octal",
    "Hexadecimal"
]

converted_number = random_number

if ( binary_base == binary ):
    converted_number = bin(random_number)
elif ( binary_base == octal ):
    converted_number = oct(random_number)
elif ( binary_base == hexadecimal ):
    converted_number = hex(random_number)

full_name_base_number = full_name_base_numbers[binary_base - 1] if binary_base > 0 and binary_base <=3 else "Decimal"
    
print()
print("- " * 50)
print()

print("Your number {} was converted to {} in base {}".format(random_number, converted_number, full_name_base_number))