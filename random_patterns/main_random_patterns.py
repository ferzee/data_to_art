from random import randint
from PIL import Image, ImageDraw
from functions import *


canvas_size = (3000, 3000)
cell_size = 50
iterations = 5

colors = [
    '#F875AA',
    '#FFDFDF',
    '#FFF6F6',
    '#AEDEFC'
]

for i in range(iterations):
    image = Image.new('RGB', canvas_size, (255, 255, 255))
    draw = ImageDraw.Draw(image)

    for x in range(0, canvas_size[0], cell_size):
        for y in range(0, canvas_size[1], cell_size):
            num = randint(0, 3)
            color = colors[num]
            cell_color = convert_hex_to_rgb(color)
            print(cell_color, color)
            draw.rectangle((x, y, x + cell_size, y + cell_size), fill=cell_color)

    image.save(f'random_pattern_{i}.png')
