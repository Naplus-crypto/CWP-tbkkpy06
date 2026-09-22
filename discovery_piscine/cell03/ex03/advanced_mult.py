#!/usr/bin/env python3
import sys

mult = 0
if (len(sys.argv) > 1):
	print("none")
	mult = 11
while (mult <= 10):
	print(f"Table de {mult}:", end=" ")
	i = 0
	while (i <= 10):
		if (i <= 9):
			print(f"{mult * i} ", end=" ")
		if (i == 10):
			print(f"{mult * i}")
		i += 1
	mult += 1
