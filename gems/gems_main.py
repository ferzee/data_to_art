from PIL import Image, ImageDraw
import random
from gradients import *


def generate_triangle_coordinates(num_coordinates, margin):
    coordinates = []
    for _ in range(num_coordinates):
        x = random.randint(0 + margin, 3000 - margin)  # Adjust the range as needed
        y = random.randint(0 + margin, 3000 - margin)
        coordinates.append((x, y))
    return coordinates


def draw_triangles(draw, coordinates):
    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            draw.line([coordinates[i], coordinates[j]], fill="white", width=5)


for i in range(50):
    # Adjust the number of coordinates as needed
    num_coordinates = 10

    margin = 150

    # Image size
    width, height = 3000, 3000

    start_color = convert_hex_to_rgb('#9D50BB')
    end_color = convert_hex_to_rgb('#6E48AA')

    # Create a black background
    image = Image.new("RGB", (width, height))
    create_horizontal_gradient(image, width, height, start_color, end_color)

    draw = ImageDraw.Draw(image)

    # Generate random coordinates
    coordinates = generate_triangle_coordinates(num_coordinates, margin)

    # Draw triangles
    draw_triangles(draw, coordinates)

    # Save or display the image
    image.save(f"gems_{i}.png")
