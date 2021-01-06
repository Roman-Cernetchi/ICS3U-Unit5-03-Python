#!/usr/bin/env python3

# Created by: Roman Cernetchi
# Created on: January 2021
# This program converts level to percentage


def calculate_grade(level):
    # converts level to percentage

    if level == "4+":
        percent = 97
    elif level == "4":
        percent = 90
    elif level == "4-":
        percent = 83
    elif level == "3+":
        percent = 78
    elif level == "3":
        percent = 75
    elif level == "3-":
        percent = 71
    elif level == "2+":
        percent = 68
    elif level == "2":
        percent = 65
    elif level == "2-":
        percent = 61
    elif level == "1+":
        percent = 58
    elif level == "1":
        percent = 55
    elif level == "1-":
        percent = 51
    elif level == "R":
        percent = 30
    else:
        percent = -1

    return percent


def main():
    try:
        level_from_user = input("Enter the level you want converted"
                                " to a percentage: ")
        print("")

        # calls function
        grade_as_percentage = calculate_grade(level_from_user)

        if grade_as_percentage == -1:
            print("Invalid input")
        else:
            print("The percentage is {0}%".format(grade_as_percentage))

    except ValueError:
        print("This was not a number")


if __name__ == "__main__":
    main()
