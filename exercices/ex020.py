from random import shuffle

first_student = input("Type first student: ")
second_student = input("Type second student: ")
third_student = input("Type third student: ")
fourth_student = input("Type fourth student: ")

try:
    students = [first_student, second_student, third_student, fourth_student]

    shuffle(students)
    index = 1
    for student in students:
        print('student {}: {}'.format(index, student))
        index += 1

except ValueError:
    print("Something went wrong")