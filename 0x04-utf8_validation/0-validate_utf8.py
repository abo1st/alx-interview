#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    The method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    number_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for iz in data:

        mask_byte = 1 << 7

        if number_bytes == 0:

            while mask_byte & iz:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (iz & mask_1 and not (iz & mask_2)):
                    return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
