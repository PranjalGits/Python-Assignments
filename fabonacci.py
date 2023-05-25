def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

# Example usage
terms = 10  # Replace with the desired number of terms

fib_sequence = fibonacci(terms)
print("Fibonacci Series:")
for term in fib_sequence:
    print(term, end=" ")
