#!/usr/bin/python3
import sys

print("This is the name of the script:", sys.argv[0])
if len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)
else:
    N = sys.argv[1]

    if not N.isnumeric():
        print("N must be a number")
        exit(1)
    else:
        if N < 4:
            print("N must be at least 4")
            exit(1)
        else:
            print("Number of arguments:", len(sys.argv))
            print("The arguments are:" , str(sys.argv))
