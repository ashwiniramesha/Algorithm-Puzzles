#!/usr/bin/python
import os
import sys
import math

def get_squares(num1,num2):
    count = 0

    low = math.ceil(math.sqrt(num1))
    high = math.floor(math.sqrt(num2))
    return int(high-low)+1

def main():
    lines = []
    for line in sys.stdin:
        lines.append(line)

    no_of_test = int(lines[0]);
    for i in range(1,no_of_test+1):
        num1 = int(lines[i].split(" ")[0])
        num2 = int(lines[i].split(" ")[1])
        squares = get_squares(num1,num2)
        print squares

if __name__ == "__main__":
    main()
