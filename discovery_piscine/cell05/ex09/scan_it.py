#!/usr/bin/env python3
import sys, re

argc = len(sys.argv)
if (argc != 3):
	print("none")
if (argc == 3):
	kc = len(re.findall(sys.argv[1], sys.argv[2]))
	if (kc == 0):
		print("none")
	if (kc != 0):
		print(f"{kc}")
