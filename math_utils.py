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


def main():
    """Run simple checks on each function and report the results."""
    tests = [
        ("add(2, 3)", add(2, 3), 5),
        ("subtract(10, 4)", subtract(10, 4), 6),
        ("multiply(3, 7)", multiply(3, 7), 21),
        ("divide(10, 4)", divide(10, 4), 2.5),
        ("power(2, 10)", power(2, 10), 1024),
        ("modulo(17, 5)", modulo(17, 5), 2),
    ]

    passed = 0
    for label, result, expected in tests:
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {label} = {result} (expected {expected})")

    # Division and modulo by zero should raise ZeroDivisionError.
    for label, func in (("divide(1, 0)", divide), ("modulo(1, 0)", modulo)):
        try:
            func(1, 0)
            print(f"[FAIL] {label} did not raise ZeroDivisionError")
        except ZeroDivisionError as e:
            passed += 1
            print(f"[PASS] {label} raised ZeroDivisionError: {e}")

    total = len(tests) + 2
    print(f"\n{passed}/{total} tests passed.")


if __name__ == "__main__":
    main()


# Testing Vibe-It PR integration