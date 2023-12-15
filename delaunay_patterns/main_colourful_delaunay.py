from PIL import Image, ImageDraw
import numpy as np
from scipy.spatial import Delaunay
import random


def create_delaunay_triangulation(width, height, num_points, output_path):
    # Generate random points, allowing coordinates outside the image dimensions
    points = np.array([[random.uniform(-250, width+250), random.uniform(-250, height+250)] for _ in range(num_points)])

    # Create a Delaunay triangulation
    tri = Delaunay(points)

    # Create a blank image for drawing
    output_image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(output_image)

    # Draw the Delaunay triangulation with random colors for each triangle
    for simplex in tri.simplices:
        triangle = [tuple(points[i]) for i in simplex]

        # Generate a random color for each triangle
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        draw.polygon(triangle, fill=color, outline=(255, 255, 255))

    # Save the result
    output_image.save(output_path)


if __name__ == "__main__":
    image_width = 1000  # Adjust the width of the image as needed
    image_height = 1000  # Adjust the height of the image as needed
    num_random_points = 100  # Adjust the number of random points as needed
    output_image_path = "result.jpg"  # Replace with the desired output path

    create_delaunay_triangulation(image_width, image_height, num_random_points, output_image_path)
