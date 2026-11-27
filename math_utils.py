"""Basic math functions."""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Return a divided by b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def power(base, exponent):
    """Return base raised to the power of exponent."""
    return base ** exponent


def modulo(a, b):
    """Return the remainder of a divided by b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot take modulo by zero.")
    return a % b


def gcd(a, b):
    """Return the greatest common divisor of a and b (Euclidean algorithm)."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return the least common multiple of a and b (0 if either is 0)."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def fibonacci(count):
    """Return a list of the first `count` Fibonacci numbers, starting 0, 1."""
    if count < 0:
        raise ValueError("Count must be non-negative.")
    sequence = []
    a, b = 0, 1
    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def is_prime(n):
    """Return True if n is a prime number, otherwise False."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def mean(numbers):
    """Return the average of a list of numbers. Raises ValueError if empty."""
    if not numbers:
        raise ValueError("Cannot take the mean of an empty list.")
    return sum(numbers) / len(numbers)


def median(numbers):
    """Return the middle value of a list of numbers. Raises ValueError if empty."""
    if not numbers:
        raise ValueError("Cannot take the median of an empty list.")
    ordered = sorted(numbers)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def absolute_value(x):
    """Return the absolute value of x."""
    return -x if x < 0 else x


def clamp(value, low, high):
    """Return value limited to the range [low, high]. Raises ValueError if low > high."""
    if low > high:
        raise ValueError("low must not be greater than high.")
    return max(low, min(value, high))


def sign(x):
    """Return 1 if x is positive, -1 if negative, and 0 if zero."""
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def distance(x1, y1, x2, y2):
    """Return the straight-line distance between points (x1, y1) and (x2, y2)."""
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5







# Testing Vibe-It PR integration