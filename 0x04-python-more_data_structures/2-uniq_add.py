#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_uniq_set = set()
    if my_list:
        for items in my_list:
            my_uniq_set.add(items)
    return sum(my_uniq_set)
