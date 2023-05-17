#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        print('', end='')
    else:
        my_list.reverse()
        for j in range(len(my_list)):
            print("{:d}".format(my_list[j]))
