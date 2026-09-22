#!/usr/bin/env python3
import sys

if (len(sys.argv) == 2):
	print(f"{sys.argv[1].lower()}")
if (len(sys.argv) != 2):
	print("none")
