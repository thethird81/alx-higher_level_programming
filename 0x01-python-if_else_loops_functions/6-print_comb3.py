#!/usr/bin/python3
for num in range(0, 9):
    for num2 in range(num + 1, 10):
        if num != 8 or num2 != 9:
            print("{:n}{:n}".format(num, num2), end=", ")
print("{:n}{:n}".format(num, num2))
