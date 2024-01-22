from PIL import ImageDraw


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

    # Check for type validity
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

    # Check for type validity
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