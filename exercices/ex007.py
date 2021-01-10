first_grade = input('Type first grade: ')
second_grade = input('Type second grade: ')

try:
    first_grade_int = float(first_grade)
    second_grade_int = float(second_grade)
    grade_average = (first_grade_int + second_grade_int)/2
    print("First grade is {:.1f} and second grade is {:.1f} and your average is {:.1f}".format(
        first_grade_int, second_grade_int, grade_average))
except ValueError:
    print("Some grade isn't a number")
