#!/usr/bin/env python3
# Module 3
#   Programming Assignment 4
#     Prob-3.py

# <Matt Russell>

def letterGrade(score):
    # your code here
    grade = ""
    if score == 0:
        grade = "F"
    elif score == 1:
        grade = "F"
    elif score == 2:
        grade = "D"
    elif score == 3:
        grade = "C"
    elif score == 4:
        grade = "B"
    elif score == 5:
        grade = "A"
    return grade


def unitTest():
    # your test code here
    print("Grade: ", letterGrade(0))
    print("Grade: ", letterGrade(1))
    print("Grade: ", letterGrade(2))
    print("Grade: ", letterGrade(3))
    print("Grade: ", letterGrade(4))
    print("Grade: ", letterGrade(5))
if __name__ == "__main__":
    unitTest()