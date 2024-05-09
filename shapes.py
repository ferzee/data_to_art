from PIL import ImageDraw, Image
import math


def draw_hexagon(image, center_x: int, center_y: int, size: int,
                 outline_color: tuple, angle: (int, float) = 0.0, width: int = 1):
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

    # Check for type validity
    if not isinstance(center_x, int):
        raise ValueError("center_x is not an int")
    
    if not isinstance(center_y, int):
        raise ValueError("center_y is not an int")
    
    if not isinstance(size, int):
        raise ValueError("size is not an int")

    if not isinstance(angle, (int, float)):
        raise ValueError("angle is not a numeric value")
    
    if not isinstance(width, int):
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


def draw_line(image, x1, y1, x2, y2, line_color, width: int):
    """
    Draws a line between two points on the image.

    Args:
        image (PIL.Image.Image): The image on which to draw the line.
        x1 (int): X-coordinate of the starting point.
        y1 (int): Y-coordinate of the starting point.
        x2 (int): X-coordinate of the ending point.
        y2 (int): Y-coordinate of the ending point.
        line_color (tuple): The color of the line (R, G, B).
        width (int): line thickness.
    """

    # Check for type validity
    if not isinstance(x1, int) or not isinstance(y1, int) or not isinstance(x2, int) or not isinstance(y2, int):
        raise ValueError("Coordinates should be integers.")

    if not isinstance(line_color, tuple) or len(line_color) != 3:
        raise ValueError("line_color should be a tuple of three values (R, G, B).")
    
    if not isinstance(width, int):
        raise ValueError("Width should be an integer.")

    draw = ImageDraw.Draw(image)

    # Draw a line segment
    draw.line([(x1, y1), (x2, y2)], fill=line_color, width=width)


def draw_polygon_from_data_set(image, data_set: list, line_color: tuple, line_width: int, close=True, rounded=True):
    """
    Draws a polygon on the image using x1 and x2 coordinates from a dataset.

    Args:
        image (PIL.Image.Image): The image on which to draw the polygon.
        data_set (list of tuples): A list of (x1, x2) coordinate pairs.
        line_color (tuple): The color of the polygon outline (R, G, B).
        line_width (int): The width of the lines connecting the circles.
        close (bool, optional): Whether to close the polygon by connecting the first and last points (default is True).
        rounded (bool, option): whether the lines should be rendered with rounded edges (default is True).
    """

    # Check for type validity
    if not isinstance(data_set, list) or not all(isinstance(point, tuple) and len(point) == 2 for point in data_set):
        raise ValueError("Dataset should be a list of (x1, x2) coordinate pairs.")

    if not isinstance(line_color, tuple) or len(line_color) != 3:
        raise ValueError("line_color should be a tuple of three values (R, G, B).")

    if not isinstance(line_width, int):
        raise ValueError("line_width should be an int.")

    draw = ImageDraw.Draw(image)

    points = [(x1, x2) for x1, x2 in data_set]

    # Makes the circles slightly smaller than the line width to make it look more natural.
    circle_size = line_width - (line_width / 10)

    if close and len(points) >= 3:
        points.append(points[0])

    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]

        # Draw a line segment
        draw.line([x1, y1, x2, y2], fill=line_color, width=line_width)

        # Adds circles at the end of each line to simulate rounding.
        if rounded:
            draw.ellipse((x1 - circle_size / 2, y1 - circle_size / 2, x1 + circle_size / 2, y1 + circle_size / 2), fill=line_color)
            draw.ellipse((x2 - circle_size / 2, y2 - circle_size / 2, x2 + circle_size / 2, y2 + circle_size / 2), fill=line_color)

    # Connect the last point to the first point with a line
    if close and len(points) >= 3:
        x1, y1 = points[-1]
        x2, y2 = points[0]
        draw.line([x1, y1, x2, y2], fill=line_color, width=line_width)


def generate_parametric_pattern(image, width, height, parameter1, parameter2, file_name, radius):
    # Create a blank image with a white background
    draw = ImageDraw.Draw(image)

    # Define the parametric function for the pattern
    def parametric_function(u, v):
        x = math.sin(u) + parameter1 * math.cos(v)
        y = math.cos(u) + parameter2 * math.sin(v)
        return x, y

    # Set the range of parameters (adjust as needed)
    u_range = (0, 2 * math.pi, 0.1)
    v_range = (0, 2 * math.pi, 0.1)

    # Iterate through the parameter values and draw ellipses on the image
    for u in range(int((u_range[1] - u_range[0]) / u_range[2])):
        for v in range(int((v_range[1] - v_range[0]) / v_range[2])):
            u_val = u_range[0] + u * u_range[2]
            v_val = v_range[0] + v * v_range[2]
            x, y = parametric_function(u_val, v_val)

            # Map the parametric coordinates to pixel coordinates
            pixel_x = int((x + 1) * 0.5 * width)
            pixel_y = int((y + 1) * 0.5 * height)

            # Draw an ellipse at the calculated position
            ellipse_radius = radius  # Adjust the radius of the ellipse
            draw.ellipse((pixel_x - ellipse_radius, pixel_y - ellipse_radius,
                          pixel_x + ellipse_radius, pixel_y + ellipse_radius),
                         fill="white")

    # Save the image
    image.save(file_name)
