#!/usr/bin/python3
import hidden_4


if __name__ == "__main__":
    names = dir(hidden_4)
    for name in names:
        if '__' != name[:2]:
            print(name)
