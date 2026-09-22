#!/usr/bin/env python3

first_number = int(input("Enter the first number:\n"))
second_number = int(input("Enter the second number:\n"))
mult = first_number * second_number
print(f"{first_number} x {second_number} = {mult}")
if (mult < 0):
        print("This result is negative.")
if (mult == 0):
        print("This result is positive and negative.")
if (mult > 0):
        print("This result is positive.")
