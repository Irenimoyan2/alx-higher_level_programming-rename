#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    # Get the list and number of arguments
    args = len(sys.argv) - 1

    # Print the number of arguments and their list
    if args == 0:
        print("0 arguments.")
    elif args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(args))
    for i in range(args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
