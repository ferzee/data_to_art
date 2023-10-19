from PIL import ImageDraw


def linear_map(value, from_low, from_high, to_low, to_high):
    """
    Linearly maps a value from one range to another.

        Args:
            value (float): The value to be mapped.
            from_low (float): The lower bound of the original range.
            from_high (float): The upper bound of the original range.
            to_low (float): The lower bound of the target range.
            to_high (float): The upper bound of the target range.

        Returns:
            float: The mapped value in the target range.
    """

    return (value - from_low) * (to_high - to_low) / (from_high - from_low) + to_low


def convert_hex_to_rgb(hex_color: str):
    """
    Converts a hex_color value to a rgb tuple.

        Args:
            hex_color (string): The hex value to be converted.

        Returns:
            rgb_color (float): The converted rgb value.
    """

    if not isinstance(hex_color, str):
        raise ValueError("hex_color is not a string")

    rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
    
    return rgb_color


def convert_hex_to_rgb(rgb_color: tuple):
    """
    Converts a hex_color value to a rgb tuple.

        Args:
            rgb_color (float): The rgb value to be converted.

        Returns:
            hex_color (string): The converted hex value.
    """
    
    if not isinstance(rgb_color, tuple):
        raise ValueError("rgb_color is not an int")
    
    hex_color = "#{:02X}{:02X}{:02X}".format(rgb_color[0], rgb_color[1], rgb_color[2])
    
    return hex_color


def create_gradient(image, img_width: int, img_height: int, start_color: tuple, end_color: tuple):
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