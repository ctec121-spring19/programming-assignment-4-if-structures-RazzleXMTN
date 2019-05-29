#!/usr/bin/env python3
# Module 3
#   Programming Assignment 4
#     Prob-2.py

# <Matt Russell>

'''
Your IPO comment goes here
Input
process
output

'''
import math
def main():
    # your code goes here
    #Variables
    
    name = input("What is your name? ")
    wage = eval(input("What is your hourly wage? "))
    hours = eval(input("How many hours have you worked this week? "))
    #formulas
    
    othours = hours - 40
    if othours < 0:
        othours = 0
    regwage = hours * wage
    otwage = (wage * 1.5) * othours
    tax = (regwage + otwage) * 0.20
    medical = (regwage + otwage) * 0.10


    '''
    if hours >= 41:
        wage = wage * 1.5
    else: 
        hours <= 40: 
        return hours
    '''
    print()
    print("Name: ", name)
    print("Hours: ", hours)
    print("wage: ", wage)
    print("Regular wages: ", regwage)
    print("Overtime Wages: ", otwage)
    print("Total Wages: ", regwage + otwage)
    print("Tax Witholding: ", tax)
    print("Medical Withholding: ", medical)
    print("Take Home Pay: ", (regwage+otwage)-(tax+medical))
    

main()