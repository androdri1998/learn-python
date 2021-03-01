first_grade = float(input("What's your first grade? "))
second_grade = float(input("What's your second grade? "))

avg_grade = (first_grade + second_grade) / 2

grade_start_recovery = 5.1
grade_end_recovery = 6.9
grade_approved = 7

if ( avg_grade > grade_approved ):
    print("You are approved!")
elif ( avg_grade >= grade_start_recovery and avg_grade <= grade_end_recovery):
    print("You go to recovery!")
else:
    print("You are disapproved!")