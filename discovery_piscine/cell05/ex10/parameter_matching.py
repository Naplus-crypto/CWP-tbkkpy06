#!/usr/bin/env python3
import sys

if (len(sys.argv) != 2):
	print("Nope, sorry...")
if (len(sys.argv) == 2):
	s = input("What was the parameter? ").strip()
	if (s == sys.argv[1]):
		print("Good job!")
	if (s != sys.argv[1]):
		print("Nope, sorry...")

