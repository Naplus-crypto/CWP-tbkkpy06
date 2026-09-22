#!/usr/bin/env python3

to25 = int(input("Enter a number less than 25\n"))
if (to25 > 25):
	print("Error")
while (to25 <= 25):
	print(f"Inside the loop, my variable is {to25}")
	to25 += 1
