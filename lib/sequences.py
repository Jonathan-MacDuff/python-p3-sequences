#!/usr/bin/env python3

def print_fibonacci(length):
    fib = []
    for i in range(length):
        if i == 0:
            fib.append(i)
        elif i == 1:
            fib.append(i)
        else:
            b = fib[-1]
            c = fib[-2]
            d = b + c
            fib.append(d)
        
    print(fib)