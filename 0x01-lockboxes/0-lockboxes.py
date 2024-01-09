#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes or len(boxes) == 0:
        return False

    # Initialize a set to keep track of visited boxes
    visited = set()
    # Mark the first box as visited
    visited.add(0)

    # Create a stack to perform DFS
    stack = [0]

    while stack:
        current_box = stack.pop()

        # Check all keys in the current box
        for key in boxes[current_box]:
            # If the key corresponds to a box that hasn't been visited
            if key < len(boxes) and key not in visited:
                # Mark the box as visited and add it to the stack
                visited.add(key)
                stack.append(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)

# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False

