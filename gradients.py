from PIL import ImageDraw
import math
from functions import convert_hex_to_rgb


def create_complex_gradient(image, img_width: int, img_height: int, colors: list, positions: list, angle: int = 0):
    """
    Creates a gradient on the background of the image with multiple colors and positions.

    Args:
        image: the image on which to draw.
        img_width (int): the width of the image to draw on.
        img_height (int): the height of the image to draw on.
        colors (list): a list of tuples representing the gradient colors (left to right).
        positions (list): a list of floats in the range [0, 1] representing the position of each color.
        angle (int, optional): the angle of the gradient (default is 0, horizontal).
    """

    if not isinstance(img_width, int):
        raise ValueError("img_width is not an int")

    if not isinstance(colors, list):
        raise ValueError("colors is not a list of tuples")
    
    if not isinstance(positions, list):
        raise ValueError("positions is not a list of floats")
    
    if len(colors) != len(positions):
        raise ValueError("colors and positions lists must have the same length")
    
    # Check that positions are in the valid range [0, 1]
    if not all(0 <= pos <= 1 for pos in positions):
        raise ValueError("positions should be in the range [0, 1]")

    draw = ImageDraw.Draw(image)
    
    angle_rad = math.radians(angle)
    
    for x in range(img_width):
        for i in range(len(positions) - 1):
            if positions[i] <= x / img_width <= positions[i + 1]:
                p = (x / img_width - positions[i]) / (positions[i + 1] - positions[i])
                color1 = colors[i]
                color2 = colors[i + 1]
                r = int(color1[0] * (1 - p) + color2[0] * p)
                g = int(color1[1] * (1 - p) + color2[1] * p)
                b = int(color1[2] * (1 - p) + color2[2] * p)
                color = (r, g, b)
                break
        else:
            color = colors[-1]

        draw.line([(x, 0), (x, img_height)], fill=color)


def create_horizontal_gradient(image, img_width: int, img_height: int, start_color: tuple, end_color: tuple):
    """
    Creates the gradient on the background of the image.

        Args:
            image: the image on which to draw.
            img_width (int): the width of the image to draw on.
            img_heigth (int): the height of the image to draw on.
            start_color (tuple): the starting color (left color).
            end_color (tuple): the ending color (right color).
    """

    if not isinstance(img_width, int):
        raise ValueError("img_width is not an int")
    
    if not isinstance(start_color, tuple):
        raise ValueError("start_color is not a tuple")
    
    if not isinstance(end_color, tuple):
        raise ValueError("end_color is not a tuple")

    for x in range(img_width):
        r = int(start_color[0] * (1 - x / img_width) + end_color[0] * (x / img_width))
        g = int(start_color[1] * (1 - x / img_width) + end_color[1] * (x / img_width))
        b = int(start_color[2] * (1 - x / img_width) + end_color[2] * (x / img_width))

        color = (r, g, b)

        draw = ImageDraw.Draw(image)

        draw.line([(x, 0), (x, img_height)], fill=color)


def create_vertical_gradient(image, img_width: int, img_height: int, start_color: tuple, end_color: tuple):
    """
    Creates a vertical gradient on the background of the image.

    Args:
        image: the image on which to draw.
        img_width (int): the width of the image to draw on.
        img_height (int): the height of the image to draw on.
        start_color (tuple): the starting color (top color).
        end_color (tuple): the ending color (bottom color).
    """

    if not isinstance(img_height, int):
        raise ValueError("img_height is not an int")

    if not isinstance(start_color, tuple):
        raise ValueError("start_color is not a tuple")
    
    if not isinstance(end_color, tuple):
        raise ValueError("end_color is not a tuple")

    for y in range(img_height):
        r = int(start_color[0] * (1 - y / img_height) + end_color[0] * (y / img_height))
        g = int(start_color[1] * (1 - y / img_height) + end_color[1] * (y / img_height))
        b = int(start_color[2] * (1 - y / img_height) + end_color[2] * (y / img_height))

        color = (r, g, b)

        draw = ImageDraw.Draw(image)

        draw.line([(0, y), (img_width, y)], fill=color)