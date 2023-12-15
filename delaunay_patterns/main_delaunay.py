from PIL import Image, ImageDraw
import numpy as np
from scipy.spatial import Delaunay
from gradients import *
from functions import *
import random


def create_delaunay_triangulation(width, height, num_points, output_path, line_width, start_color, end_color):
    margin_lr = width / 5
    margin_tb = height / 5

    # Generate random points, allowing coordinates outside the image dimensions
    points = np.array([[random.uniform(-margin_lr, width+margin_lr), random.uniform(-margin_tb, height+margin_tb)]
                       for _ in range(num_points)])

    # Create a Delaunay triangulation
    tri = Delaunay(points)

    # Create a blank image for drawing
    output_image = Image.new("RGB", (width, height))
    create_horizontal_gradient(output_image, width, height, start_color, end_color)
    draw = ImageDraw.Draw(output_image)

    # Draw the Delaunay triangulation
    for simplex in tri.simplices:
        triangle = [tuple(points[i]) for i in simplex]
        draw.polygon(triangle, outline=(255, 255, 255), width=line_width)

    # Save the result
    output_image.save(output_path)


if __name__ == "__main__":
    for i in range(1):
        image_width = 3000  # Adjust the width of the image as needed
        image_height = 3000  # Adjust the height of the image as needed
        num_random_points = 100  # Adjust the number of random points as needed
        output_image_path = f"result_{i}.png"  # Replace with the desired output path
        thickness = 2
        start_color = convert_hex_to_rgb('#00273C')
        end_color = convert_hex_to_rgb('#00273C')

        create_delaunay_triangulation(image_width, image_height, num_random_points, output_image_path, thickness, start_color, end_color)
