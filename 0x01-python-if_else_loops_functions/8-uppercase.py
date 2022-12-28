#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            s = ord(s) - 32
            s = chr(s)
        print("{}".format(s), end="")
    print("")
