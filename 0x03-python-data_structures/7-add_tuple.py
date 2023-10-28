#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup_c = ()
    mx = max(len(tuple_a), len(tuple_b))
    if len(tuple_b) == 1:
        tuple_b = (tuple_b[0] + 0, 0)
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    if len(tuple_a) > 2 or len(tuple_b) > 2:
        tuple_a = (0, 0)
        tuple_b = (0, 0)
    for i in range(1):
        tup_c = (tuple_a[i] + tuple_b[i], tuple_a[i + 1] + tuple_b[i + 1])
    return tup_c
