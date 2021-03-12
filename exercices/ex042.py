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

    is_a_valid_triangle = is_first_line_valid and is_second_line_valid and is_third_line_valid
    type_triangle = ""
    if ( is_a_valid_triangle ):
        if first_line == second_line == third_line:
            type_triangle = "This is a equilateral triangle"
        elif first_line != second_line != third_line != first_line:
            type_triangle = "This is a scalene triangle"
        else:
            type_triangle = "This is a isosceles triangle"

    print()
    print("- " * 50)
    print()

    print("It's a valid triangle" if is_a_valid_triangle else "It isn't a valid triangle")
    print(type_triangle)
    
except ValueError:
    print("Some value isn't a number")