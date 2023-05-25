def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = 5  # Replace with the desired integer

result = factorial(number)
print(f"The factorial of {number} is: {result}")
