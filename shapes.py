from PIL import ImageDraw
import math


def draw_hexagon(image, center_x: int, center_y: int, size: int, outline_color: tuple, angle: float = 0.0, width: int = 1):
    """
    Draws a hexagon.

        Args:
            image (PIL.Image.Image): the PIL image on which to draw the hexagon.
            center_x (int): The x-coordinate of the center of the hexagon.
            center_y (int): The y-coordinate of the center of the hexagon.
            size (int): The size of the hexagon (distance from center to vertex).
            outline_color (tuple, optional): The outline color of the hexagon (R, G, B).
            angle (float, optional): The rotation angle of the hexagon in degrees (default is 0.0).
            width (int, optional): The thickness of the line (default is 1).
    """

    # Check if the right types are being used
    if not isinstance(center_x, int):
        raise ValueError("center_x is not an int")
    
    if not isinstance(center_y, int):
        raise ValueError("center_y is not an int")
    
    if not isinstance(size, int):
        raise ValueError("size is not an int")

    if not isinstance(angle, (int, float)):
        raise ValueError("angle is not a numeric value")
    
    if not isinstance(width, (int)):
        raise ValueError("angle is not an int")

    draw = ImageDraw.Draw(image)

    angle_rad = math.radians(angle)
    angle_step = 360 / 6

    points = []

    for i in range(6):
        # Calculate the rotated coordinates
        x = center_x + size * 2 * (3 ** 0.5 / 2) * math.cos(angle_rad + math.radians(angle_step * i))
        y = center_y + size * 2 * (3 ** 0.5 / 2) * math.sin(angle_rad + math.radians(angle_step * i))
        points.append((x, y))

    draw.polygon(points, outline=outline_color, width=width)
