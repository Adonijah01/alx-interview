#!/usr/bin/python3

def minOperations(n):
    """
    Calculates the fewest number of operations needed to get n H characters.

    Args:
    - n: an integer, the target number of H characters.

    Returns:
    - An integer, the minimum number of operations required.
      If n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

if __name__ == "__main__":
    # Test cases
    n1 = 4
    n2 = 12

    result1 = minOperations(n1)
    result2 = minOperations(n2)

    print("Min # of operations to reach {} char: {}".format(n1, result1))
    print("Min # of operations to reach {} char: {}".format(n2, result2))

