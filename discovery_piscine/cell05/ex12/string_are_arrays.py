#!/usr/bin/env python3
import sys

argc = len(sys.argv)
if (argc != 2):
	print("none")
if (argc == 2):
	count = sys.argv[1].count('z')
	if (count == 0):
		print("none")
	if (count >= 1):
		print("z" * count)
