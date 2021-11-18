#!/usr/bin/python3
for r in range(0, 9):
    for t in range(r + 1, 10):
        if r == 8:
            print("{}{}".format(r, t))
        else:
            print("{}{}".format(r, t), end=", ")
