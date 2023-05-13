#!/usr/bin/python3
start, end = ord('A'), ord('Z')
print(*map(chr, range(start, end+1)), sep='', end='\n')
