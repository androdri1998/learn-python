from random import choice

first_student = input("Type first student: ")
second_student = input("Type second student: ")
third_student = input("Type third student: ")
fourth_student = input("Type fourth student: ")

try:
    students = [first_student, second_student, third_student, fourth_student]
    
    drawn_student = choice(students)
    print('The drawn student is {}'.format(drawn_student))

except ValueError:
    print("Something went wrong")