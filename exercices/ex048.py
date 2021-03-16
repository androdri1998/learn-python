total = 0

for index in range(1, 501):
    if(index%3 == 0):
        total = total + index

print("The sum total from multiples of 3 from 1 until 500 is {}".format(total))
