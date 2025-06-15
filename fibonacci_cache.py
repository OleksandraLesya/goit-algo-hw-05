"""
Module: caching_fibonacci
This module provides a closure-based implementation of the Fibonacci sequence 
calculator with internal caching (memoization) for improved performance.
Functions:
- caching_fibonacci: Returns a Fibonacci function with built-in caching.
"""
def caching_fibonacci():
    """
    Creates and returns an inner function `fibonacci` that calculates
    Fibonacci numbers using caching (memoization).
    The cache (`cache` dictionary) stores already computed values,
    which avoids repeated recursive calculations and significantly
    optimizes performance for large Fibonacci numbers.
    Returns:
        function: The inner function `fibonacci(n)`, which takes an integer `n`
                  and returns the n-th Fibonacci number.
    """
    cache = {}  # Stores already computed Fibonacci values

    def fibonacci(n):
        """
        Calculates the n-th Fibonacci number, using the cache of the outer function.
        Args:
            n (int): The position of the Fibonacci number to compute.
        Returns:
            int: The n-th Fibonacci number.
        """
        # Base cases for recursion
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # Return from cache if already computed
        if n in cache:
            return cache[n]
        # Recursively compute and store in cache
        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result

    return fibonacci

# Example usage of the function:
fib = caching_fibonacci()

print(fib(10))  # Expected output: 55
print(fib(15))  # Expected output: 610
print(fib(35))  # Expected output: 9227465 (fast, thanks to caching)
# print(fib(50)) # You can try a large number to see the benefits of caching
