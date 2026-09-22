#!/usr/bin/env python3
import sys

argc = len(sys.argv)
if (argc == 1):
	print("none")
if (argc != 1):
	print(f"parameters: {argc - 1}")
	i = 1
	while (i != (argc)):
		print(f"{sys.argv[i]}: {len(sys.argv[i])}")
		i += 1
