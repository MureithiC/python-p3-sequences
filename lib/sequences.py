#!/usr/bin/env python3

def print_fibonacci(length):

	list_fib = []
	if length > 0:
		list_fib.append(0)
	if length >= 2:
		list_fib.append(1)
		for i in range(2, length):
			list_fib.append(list_fib[-1] + list_fib[-2])

	print(list_fib)