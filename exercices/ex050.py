even_numbers = []
for index in range(1,7):
    number = int(input('Type a number: '))
    if(number%2 == 0):
        even_numbers.append(str(number))

str_even_numbers = ", ".join(even_numbers)

print("even numbers are {}".format(str_even_numbers))