try:
    first_line = float(input("Type first line's length: "))
    second_line = float(input("Type second line's length: "))
    third_line = float(input("Type third line's length: "))

    sum_to_validate_first_line = second_line + third_line
    difference_to_validate_first_line = second_line - third_line
    is_first_line_valid = False
    if(difference_to_validate_first_line < first_line and first_line < sum_to_validate_first_line):
        is_first_line_valid = True

    sum_to_validate_second_line = first_line + third_line
    difference_to_validate_second_line = first_line - third_line
    is_second_line_valid = False
    if(difference_to_validate_second_line < second_line and second_line < sum_to_validate_second_line):
        is_second_line_valid = True

    sum_to_validate_third_line = first_line + second_line
    difference_to_validate_third_line = first_line - second_line
    is_third_line_valid = False
    if(difference_to_validate_third_line < third_line and third_line < sum_to_validate_third_line):
        is_third_line_valid = True

    print("It's a valid triangle" if is_first_line_valid and is_second_line_valid and is_third_line_valid else "It isn't a valid triangle")

except ValueError:
    print("Some value isn't a number")