#!/usr/bin/python3
for num in range(0, 100):
    if num < 99:
        print("{:02n}".format(num), end=", ")
    else:
        print("{:02n}".format(num))
