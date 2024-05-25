# lib/sequences.py

def print_fibonacci(length):
    if length == 0:
        print([])
        return

    fibonacci_sequence = [0]  # Initialize Fibonacci sequence with the first number
    if length > 1:
        fibonacci_sequence.append(1)  # Append the second number if length is greater than 1

    while len(fibonacci_sequence) < length:  # Keep generating Fibonacci numbers until desired length is reached
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]  # Calculate next Fibonacci number
        fibonacci_sequence.append(next_fibonacci)  # Add next Fibonacci number to the sequence
    
    print(fibonacci_sequence)
