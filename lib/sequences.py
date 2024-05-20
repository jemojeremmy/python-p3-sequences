#!/usr/bin/env python3

def print_fibonacci(length):
    # Initialize the list with the first two Fibonacci numbers
    fibonacci_sequence = [0, 1]

    # If the desired length is less than 2, slice the list accordingly
    if length <= 0:
        print([])
        return
    elif length == 1:
        print([0])
        return

    # Generate the Fibonacci sequence up to the desired length
    while len(fibonacci_sequence) < length:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)

    # Print the resulting list up to the desired length
    print(fibonacci_sequence[:length])