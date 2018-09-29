#!/usr/bin/env python3.6

import sys


def read_file():
    file_open = open(sys.argv[1], "r")
    file_data = file_open.readlines()
    file_data[0] = file_data[0].rstrip()
    file_data[1] = file_data[1].rstrip()

    if len(file_data[0]) != len(file_data[1]):
        sys.exit(84)

    xored = hex(int(file_data[0].strip(), 16) ^ int(file_data[1].strip(), 16)).lstrip('0x')
    if len(xored) % 2 == 1:
        xored = '0' + xored
    print(xored.upper())


if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit(84)
    try:
        read_file()
    except IOError:
        sys.exit(84)
    sys.exit(0)