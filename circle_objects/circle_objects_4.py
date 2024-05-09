from PIL import Image, ImageDraw
from random import randint
from scipy.spatial import Delaunay
import functions

for file in range(5):
    IMG_HEIGHT = 3000
    IMG_WIDTH = 3000
    MARGIN = 300

    BG_COLOR = functions.convert_hex_to_rgb('#4c3642')
    LINE_COLOR = functions.convert_hex_to_rgb('#FFFFFF')

    image = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), BG_COLOR)

    draw = ImageDraw.Draw(image)

    bounding_box = (
        MARGIN,
        MARGIN,
        IMG_WIDTH - MARGIN,
        IMG_HEIGHT - MARGIN
    )

    # Draw big circle
    draw.ellipse(xy=bounding_box, fill=None, outline=LINE_COLOR, width=30)

    points = []

    for i in range(25):
        random_angle = randint(0, 360)
        xy = functions.point_on_circle(bounding_box, random_angle)

        points.append(xy)

    for i in range(25):
        new_circle_width = randint(0, IMG_WIDTH - (MARGIN * 2))

        new_bounding_box = functions.calc_bounding_box_from_center([1500, 1500], new_circle_width)
        random_angle = randint(0, 360)

        new_xy = functions.point_on_circle(new_bounding_box, random_angle)

        points.append(new_xy)

    tri = Delaunay(points)

    for simplex in tri.simplices:
        triangle = [tuple(points[i]) for i in simplex]
        draw.polygon(triangle, outline=LINE_COLOR, width=5)

    image.save(f'circle_delauney_triangulation_{file}.png')

    #image.show()