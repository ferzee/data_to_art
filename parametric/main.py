from shapes import *
from gradients import *
from PIL import Image
import random

for i in range(50):
    img_width = 3000
    img_height = 3000

    factor = int(img_height / 1000) * 2

    image = Image.new('RGB', (img_width, img_height))

    start_color = convert_hex_to_rgb("#00d2ff")
    end_color = convert_hex_to_rgb("#3a7bd5")

    create_horizontal_gradient(image, img_width, img_height, start_color, end_color)

    param_a = random.random()
    param_b = random.random()
    file_name = f"file_{i}.png"
    radius = 10
    generate_parametric_pattern(image, img_width, img_height, param_a, param_b, file_name, radius)


