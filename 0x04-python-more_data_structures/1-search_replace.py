#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lis = []
    for x in my_list:
        if x != search:
            lis = x
        else:
            lis = replace 
    return lis
