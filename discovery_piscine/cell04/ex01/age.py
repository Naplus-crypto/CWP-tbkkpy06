#!/usr/bin/env python3

age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old.")
years = 10
while (years <= 30):
	print(f"In {years} years, you'll be {age + years} years old.")
	years += 10
