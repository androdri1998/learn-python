from math import trunc
number_value = input("Type a number between 0 and 9999: ")

try:
    number = int(number_value)
    if(number >= 0 and number <= 9999):
        amount_thousands = trunc(number / 1000)
        thousands = amount_thousands * 1000

        hundreds_value = number - thousands
        amount_hundreds = trunc(hundreds_value / 100)
        hundreds = amount_hundreds * 100

        dozens_value = number - (thousands + hundreds)
        amount_dozens = trunc(dozens_value / 10)
        dozens = amount_dozens * 10

        units_value = number - (thousands + hundreds + dozens)

        print("-" * 50)
        print("Calculation with number" )
        print("-" * 50)

        print("{} Thousands".format(amount_thousands))
        print("{} Hundreds".format(amount_hundreds))
        print("{} Dozens".format(amount_dozens))
        print("{} Units".format(units_value))

        number_formatted = "{:0>4}".format(number_value)
        thousands_in_string = number_formatted[0]
        hundreds_in_string = number_formatted[1]
        dozens_in_string = number_formatted[2]
        units_in_string = number_formatted[3]

        print("-" * 50)
        print("Calculation with string")
        print("-" * 50)

        print("{} Thousands".format(thousands_in_string))
        print("{} Hundreds".format(hundreds_in_string))
        print("{} Dozens".format(dozens_in_string))
        print("{} Units".format(units_in_string))

    else:
        print("Value isn't in valid range")
except ValueError:
    print("Value isn't a number")
