def fibonacci(n):

    # Check if the input is valid

    if n <= 0:

        return []

    elif n == 1:

        return [0]

    elif n == 2:

        return [0, 1]

    

    # Generate the Fibonacci series

    fib_series = [0, 1]  # Starting with the first two numbers

    

    while len(fib_series) < n:

        next_num = fib_series[-1] + fib_series[-2]  # Calculate the next Fibonacci number

        fib_series.append(next_num)

    

    return fib_series

# Test the function

num_terms = int(input("Enter the number of terms in the Fibonacci series: "))

fib_result = fibonacci(num_terms)

print("Fibonacci series:", fib_result)
