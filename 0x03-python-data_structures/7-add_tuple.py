#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup_a = tuple_a[:2] + (0, 0)
    tup_b = tuple_b[:2] + (0, 0)
    sum_tuple = (tup_a[0] + tup_b[0], tup_a[1] + tup_b[1])
    return sum_tuple
