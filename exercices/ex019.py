from random import randint

first_student = input("Type first student: ")
second_student = input("Type second student: ")
third_student = input("Type third student: ")
fourth_student = input("Type fourth student: ")

try:
    students = [first_student, second_student, third_student, fourth_student]
    random_number = randint(0, 3)
    
    drawn_student = students[random_number]
    print('The drawn student is {}'.format(drawn_student))

except ValueError:
    print("Some value isn't a number")