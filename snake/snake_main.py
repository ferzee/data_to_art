from PIL import Image, ImageDraw
import random
from functions import *
from gradients import create_vertical_gradient


# Set up constants
line_width = 5
image_size = 3000
grid_distance = 150
margin = 300


for file in range(5):

    # Create a black image
    image = Image.new("RGB", (image_size, image_size), "black")
    draw = ImageDraw.Draw(image)

    start_color = convert_hex_to_rgb('#E44D26')
    end_color = convert_hex_to_rgb('#F16529')

    create_vertical_gradient(image, image_size, image_size, start_color, end_color)

    total_coords = []

    for iteration in range(15):
        x = random.randint(1, 9) * (image_size / 10)
        y = random.randint(1, 9) * (image_size / 10)

        temp_x = x
        temp_y = y

        length = 50

        coords = [(x, y)]

        for i in range(length):

            if random.choice([True, False]):
                if random.choice([True, False]):
                    if x < image_size - margin:
                        temp_x = x + grid_distance
                else:
                    if x > margin:
                        temp_x = x - grid_distance
            else:
                if random.choice([True, False]):
                    if y < image_size - margin:
                        temp_y = y + grid_distance
                else:
                    if y > margin:
                        temp_y = y - grid_distance

            if (temp_x, temp_y) not in coords and (temp_x, temp_y) not in total_coords:
                coords.append((temp_x, temp_y))
                x = temp_x
                y = temp_y
            else:
                temp_x = x
                temp_y = y


        i = 0

        for coord in coords:
            total_coords.append(coord)
            if i < len(coords)-1:
                draw.line(xy=(coords[i], coords[i+1]), width=line_width)

                i += 1





    # Save or display the image
    image.save(f"lines_{file}.png")

