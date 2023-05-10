#!/usr/bin/python3
for letter_code in range(97, 123):
    if chr(letter_code) not in ['e', 'q']:
        print("{}".format(chr(letter_code)), end="")
