firstGrade = input('Type first grade: ')
secondGrade = input('Type second grade: ')

if firstGrade.isnumeric() and secondGrade.isnumeric():
    firstGradeInt = int(firstGrade)
    secondGradeInt = int(secondGrade)
    gradeAverage = (firstGradeInt + secondGradeInt)/2
    print("First grade is {} and second grade is {} and your average is {:.2f}".format(
        firstGradeInt, secondGradeInt, gradeAverage))
else:
    print("Some grade isn't a number")
