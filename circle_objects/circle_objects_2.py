from PIL import Image, ImageDraw
from random import randint
import functions


for file in range(5):
    IMG_HEIGHT = 3000
    IMG_WIDTH = 3000
    MARGIN = 300

    BG_COLOR = functions.convert_hex_to_rgb('#f2f2f2')
    LINE_COLOR = functions.convert_hex_to_rgb('#1D1D1E')

    image = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), BG_COLOR)

    draw = ImageDraw.Draw(image)

    bounding_box = functions.calc_bounding_box(MARGIN, IMG_HEIGHT)

    radius = (bounding_box[2] - bounding_box[0]) / 2
    center_x = bounding_box[0] + radius
    center_y = bounding_box[1] + radius

    for i in range(20):
        random_angles = [
            functions.point_on_circle(bounding_box, randint(0, 180)),
            functions.point_on_circle(bounding_box, randint(181, 360))
        ]

        draw.line(xy=random_angles, fill=LINE_COLOR, width=30)

    offset = 15


    bounding_box = functions.calc_bounding_box(MARGIN, IMG_HEIGHT, offset)

    draw.ellipse(xy=bounding_box, fill=None, outline=LINE_COLOR, width=30)

    image.save(f'circle_with_lines_{file}.png')
