#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as argv
    if len(argv) == 0:
        print("0")
    else:
        result = 0
        for i in range(1, len(argv)):
            result += int(argv[i])
        print("{}".format(result))
