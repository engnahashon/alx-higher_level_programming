#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    indx = 0
    for i in my_list:
        if i % 2 == 0:
            new_list[indx] = True
        else:
            new_list[indx] = False
        indx += 1
    return (new_list)
