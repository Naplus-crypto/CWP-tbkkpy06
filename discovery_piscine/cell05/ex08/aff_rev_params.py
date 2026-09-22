#!/usr/bin/env python3
import sys

pc = len(sys.argv) - 1
if (pc <= 1):
	print("none")
if (pc > 1):
	while (pc != 0):
		print(f"{sys.argv[pc]}")
		pc -= 1
