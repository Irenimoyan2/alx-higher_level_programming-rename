#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
    print("{} the string is greater".format(number))
elif number == 0:
    print("{} the string is zero".format(number))
else:
    print("{} the string is less 6 not 0".format(number))

