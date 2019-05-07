#!/usr/bin/env python3
# Module 3
#   Programming Assignment 4
#     Prob-5.py

# <Matt Russell>

def main():
    try:
        x = eval(2)
        print("x:", x)
    except TypeError:
        print("Type Error")
    except:
        print("general error")

main()