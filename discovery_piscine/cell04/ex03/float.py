#!/usr/bin/env python3

number = float(input("Give me a number: "))
if (number.is_integer()):
	print("This number is an integer.")
if (number.is_integer() == False):
	print("This number is a decimal.")
