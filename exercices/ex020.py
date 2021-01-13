from random import randint

first_student = input("Type first student: ")
second_student = input("Type second student: ")
third_student = input("Type third student: ")
fourth_student = input("Type fourth student: ")

def order_by_number(student):
    return student['number']

try:
    students = [
        {
            'name': first_student,
            'number': randint(0, 100)
        }, 
        {
            'name': second_student,
            'number': randint(0, 100)
        }, 
        {
            'name': third_student,
            'number': randint(0, 100)
        }, 
        {
            'name': fourth_student,
            'number': randint(0, 100)
        }
    ]

    students.sort(key=order_by_number)

    index = 1
    print()
    print("Sorted list of the draw: ")
    print("-" * 30)
    for student in students:
        print('student {}: {}'.format(index, student['name']))
        index += 1

except ValueError:
    print("Something went wrong")