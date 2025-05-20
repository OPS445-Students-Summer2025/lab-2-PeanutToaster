#!/usr/bin/env python3
# Ricky Tang - 104448246
import sys

if len(sys.argv) != 3: #run error message if arguments not equal to 3
    print("Usage: " + sys.argv[0] + " name age")
    sys.exit(0)

else:
    name = sys.argv[1]
    age = sys.argv[2]
    print('Hi ' + name + ', you are ' + str(age) + ' years old.')

