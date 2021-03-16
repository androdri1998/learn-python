first_term = int(input('Type initial number of arithmetic progression: '))
reason_arithmetic_progression = int(input('Type the reason of arithmetic progression: '))

total = first_term
for index in range(0, 10):
    print(total)
    total = total + reason_arithmetic_progression