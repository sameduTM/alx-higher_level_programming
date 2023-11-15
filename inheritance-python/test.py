#!/usr/bin/python3

def hello(*args, **kwargs):
    if kwargs:
        print("kwargs:", kwargs)
    print(type(kwargs))
    print(dir(kwargs))
    
hello(what='world')