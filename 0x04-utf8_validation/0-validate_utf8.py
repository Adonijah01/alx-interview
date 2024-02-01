#!/usr/bin/python3
"""
Validates if a given dataset represents a valid UTF-8 encoding.
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing the data set.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes to check for each character
    num_bytes_to_check = 0

    for num in data:
        # Check if it's a continuation byte
        if num_bytes_to_check == 0:
            if (num >> 7) == 0b0:
                continue
            elif (num >> 5) == 0b110:
                num_bytes_to_check = 1
            elif (num >> 4) == 0b1110:
                num_bytes_to_check = 2
            elif (num >> 3) == 0b11110:
                num_bytes_to_check = 3
            else:
                return False
        else:
            # Check if the current byte is a valid continuation byte
            if (num >> 6) == 0b10:
                num_bytes_to_check -= 1
            else:
                return False

    # Check if there are incomplete characters
    return num_bytes_to_check == 0

if __name__ == "__main__":
    # Example usage
    data1 = [65]
    print(validUTF8(data1))  # Should print: True

    data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))  # Should print: True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # Should print: False

