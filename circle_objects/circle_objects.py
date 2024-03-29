from PIL import Image, ImageDraw
from random import randint
import functions


for file in range(1):
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

    radius = (bounding_box[2] - bounding_box[0]) / 2
    center_x = bounding_box[0] + radius
    center_y = bounding_box[1] + radius

    draw.ellipse(xy=bounding_box, fill=None, outline=LINE_COLOR, width=30)

    num_str = functions.create_random_num_str(randint(8, 14))

    parts = functions.convert_num_string(num_str)

    num_of_circles = len(parts)

    circle_width_range = [300, 2000]
    
    for i in range(num_of_circles):

        circle_width = functions.linear_map(int(parts[i]), 0, 100, circle_width_range[0], circle_width_range[1])

        new_bounding_box = functions.calc_inner_circle(bounding_box, circle_width)

        random_angle = functions.linear_map(int(parts[i]), 0, 100, circle_width_range[0], circle_width_range[1])

        rand_circle_xy = functions.point_on_circle(new_bounding_box, random_angle)

        fill_colour = functions.convert_hex_to_rgb('#FFFFFF')

        draw.ellipse(xy=functions.calc_bounding_box(rand_circle_xy, circle_width), fill=None, outline=LINE_COLOR, width=30)


    #image.save(f'{num_str}.png')

    image.show()