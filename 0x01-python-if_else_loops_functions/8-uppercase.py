#!/usr/bin/python3
def uppercase(s):
    result = ""
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
