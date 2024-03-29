"""
Includes all helper functions
"""

import math
from random import randint


def linear_map(value: (int, float), from_low: (int, float), from_high: (int, float),
               to_low: (int, float), to_high: (int, float)):
    """
    Linearly maps a value from one range to another.

        Args:
            value (int, float): The value to be mapped.
            from_low (int, float): The lower bound of the original range.
            from_high (int, float): The upper bound of the original range.
            to_low (int, float): The lower bound of the target range.
            to_high (int, float): The upper bound of the target range.

        Returns:
            float: The mapped value in the target range.
    """

    # Check for type validity
    if not isinstance(value, (int, float)):
        raise ValueError("value should be an int or a float")

    if not isinstance(from_low, (int, float)):
        raise ValueError("from_low should be an int or a float")

    if not isinstance(from_high, (int, float)):
        raise ValueError("from_high should be an int or a float")

    if not isinstance(to_low, (int, float)):
        raise ValueError("to_low should be an int or a float")

    if not isinstance(to_high, (int, float)):
        raise ValueError("to_high should be an int or a float")

    return (value - from_low) * (to_high - to_low) / (from_high - from_low) + to_low


def convert_hex_to_rgb(hex_color: str):
    """
    Converts a hex_color value to a rgb tuple.

        Args:
            hex_color (string): The hex value to be converted.

        Returns:
            rgb_color (float): The converted rgb value.
    """

    # Check for type validity
    if not isinstance(hex_color, str):
        raise ValueError("hex_color is not a string")

    rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
    
    return rgb_color


def convert_rgb_to_hex(rgb_color: tuple):
    """
    Converts a hex_color value to a rgb tuple.

        Args:
            rgb_color (float): The rgb value to be converted.

        Returns:
            hex_color (string): The converted hex value.
    """

    # Check for type validity
    if not isinstance(rgb_color, tuple):
        raise ValueError("rgb_color is not a tuple")
    
    hex_color = "#{:02X}{:02X}{:02X}".format(rgb_color[0], rgb_color[1], rgb_color[2])
    
    return hex_color


def point_on_circle(bounding_box, angle_degrees):
    angle_degrees = angle_degrees - 90
    # Calculate center of the bounding box
    center_x = (bounding_box[0] + bounding_box[2]) / 2
    center_y = (bounding_box[1] + bounding_box[3]) / 2

    # Calculate radius of the circle
    radius = min((bounding_box[2] - bounding_box[0]) / 2, (bounding_box[3] - bounding_box[1]) / 2)

    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)

    # Calculate x and y coordinates
    x = center_x + radius * math.cos(angle_radians)
    y = center_y + radius * math.sin(angle_radians)

    return x, y


def calc_inner_circle(bounding_box, small_circles_width):
    inner_circle_bounding_box = (
        bounding_box[0] + small_circles_width / 2,
        bounding_box[1] + small_circles_width / 2,
        bounding_box[2] - small_circles_width / 2,
        bounding_box[3] - small_circles_width / 2,
    )

    return inner_circle_bounding_box


def calc_bounding_box(margin, size, offset=0):
    bounding_box = (
        margin - offset,
        margin - offset,
        size - margin + offset,
        size - margin + offset
    )

    return bounding_box


def calc_bounding_box_from_center(xy, circle_width, offset=0):
    bounding_box = (
        (xy[0] - circle_width / 2) - offset,
        (xy[1] - circle_width / 2) - offset,
        (xy[0] + circle_width / 2) + offset,
         (xy[1] + circle_width / 2 + offset)
    )

    return bounding_box


def convert_num_string(num):
    num_string = str(num)

    parts = []

    if len(num_string) % 2 != 0:
        num_string += "0"

    parts_num = int(len(num_string) / 2)

    current_num = 0
    for i in range(parts_num):
        part_string = ""
        part_string += num_string[current_num]
        part_string += num_string[current_num + 1]
        parts.append(part_string)

        current_num += 2

    return parts


def create_random_num_str(length):
    result_str = ""
    for i in range(length):
        num = str(randint(0, 9))
        result_str += num

    return int(result_str)



