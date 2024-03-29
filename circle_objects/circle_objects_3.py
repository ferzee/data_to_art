from PIL import Image, ImageDraw
from random import randint
import functions

for file in range(5):
    IMG_HEIGHT = 3000
    IMG_WIDTH = 3000
    MARGIN = 300

    BG_COLOR = functions.convert_hex_to_rgb('#FFFFFF')
    LINE_COLOR = functions.convert_hex_to_rgb('#000000')

    image = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), BG_COLOR)

    draw = ImageDraw.Draw(image)

    bounding_box = (
        MARGIN,
        MARGIN,
        IMG_WIDTH - MARGIN,
        IMG_HEIGHT - MARGIN
    )

    circle_width = randint(500, 2000)
    # circle_width = (IMG_WIDTH - (MARGIN * 2)) / 2

    radius = (bounding_box[2] - bounding_box[0]) / 2
    center_x = bounding_box[0] + radius
    center_y = bounding_box[1] + radius

    draw.ellipse(xy=bounding_box, fill=None, outline=LINE_COLOR, width=30)

    num_of_circles = randint(4, 20)

    part_size = 360 / num_of_circles

    angle = 0

    for i in range(num_of_circles):

        new_bounding_box = functions.calc_inner_circle(bounding_box, circle_width)

        rand_circle_xy = functions.point_on_circle(new_bounding_box, angle)

        fill_colour = functions.convert_hex_to_rgb('#FFFFFF')

        draw.ellipse(xy=functions.calc_bounding_box_from_center(rand_circle_xy, circle_width), fill=None, outline=LINE_COLOR,
                     width=30)

        angle += part_size

    # image.save(f'{num_str}.png')

    image.show()