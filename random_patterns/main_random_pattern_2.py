from PIL import Image, ImageDraw
import random
from functions import *
from gradients import create_vertical_gradient


for iteration in range(5):
    # Set up constants
    line_width = 5
    grid_size = 15
    square_size = 200
    large_square_size = 300
    image_size = grid_size * square_size + line_width

    # Create a black image
    image = Image.new("RGB", (image_size, image_size), "black")
    draw = ImageDraw.Draw(image)

    start_color = convert_hex_to_rgb('#4b6cb7')
    end_color = convert_hex_to_rgb('#182848')

    create_vertical_gradient(image, image_size, image_size, start_color, end_color)



    # Set to keep track of drawn squares
    drawn_squares = set()

    # Draw the grid of squares with white outlines
    for i in range(grid_size):
        for j in range(grid_size):
            x = i * square_size
            y = j * square_size

            # Randomly choose whether to draw a large square if the position is not occupied
            if (i, j) not in drawn_squares and random.choice([True, False]):
                size = large_square_size
                draw.rectangle([x, y, x + size, y + size], outline="white", width=line_width)

                # Mark the position as occupied
                for k in range(size // square_size):
                    for l in range(size // square_size):
                        drawn_squares.add((i + k, j + l))


    #draw square around the borders
    draw.rectangle([0, 0, image_size, image_size], outline="white", width=line_width)


    # Save or display the image
    image.save(f"grid{iteration}.png")
