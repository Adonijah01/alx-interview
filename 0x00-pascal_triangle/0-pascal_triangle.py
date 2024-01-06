def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
    - n: An integer representing the number of rows in Pascal's Triangle.

    Returns:
    - A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1] + [prev_row[j - 1] + prev_row[j] for j in range(1, i)] + [1]
        triangle.append(new_row)

    return triangle


# Test the function with the provided script
if __name__ == "__main__":
    pascal_triangle_result = pascal_triangle(5)
    print_triangle(pascal_triangle_result)

