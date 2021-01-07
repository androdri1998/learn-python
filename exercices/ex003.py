
def sum_two_numbers(first_number, second_number):
    if first_number.isnumeric():
        first_number_int = int(first_number)
    else:
        return None

    if second_number.isnumeric():
        second_number_int = int(second_number)
    else:
        return None

    total = first_number_int + second_number_int
    return total


first_number = input('First number: ')
second_number = input('Second number: ')

result = sum_two_numbers(first_number, second_number)

if result != None:
    print('The sum between {} + {} is: {}'.format(first_number, second_number, result))
else:
    print("No have result!")
