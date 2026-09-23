#!/usr/bin/env python3
import sys

argc = len(sys.argv)
if (argc == 1):
    print("none")
if (argc > 1):
    i = 1
    while (argc != i):
        if not(sys.argv[i].endswith('ism')):
            print(f"{sys.argv[i]}ism")
        i += 1
