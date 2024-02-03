from PIL import Image, ImageDraw
import random


img_width = 3000
img_height = 3000
cell_width = 30
cell_height = 30
circle_radius = (cell_width / 3) / 2
rows = int(img_width / cell_width)
cols = int(img_height / cell_height)

# https://uigradients.com/#Aubergine?


for iteration in range(5):

    image = Image.new("RGB", (img_width, img_height), "black")
    draw = ImageDraw.Draw(image)

    xy_points = []

    for i in range(rows):
        x_point = i * cell_width
        if i > 0:
            for j in range(cols):
                if j > 0:
                    y_point = j * cell_height
                    xy_point = [x_point, y_point]
                    xy_points.append(xy_point)

    for xy_point in xy_points:
        ellipse_xy = (
            (xy_point[0] - circle_radius, xy_point[1] - circle_radius),
            (xy_point[0] + circle_radius, xy_point[1] + circle_radius)
        )

        draw_choice = random.choice([True, False])

        if draw_choice:
            draw.ellipse(ellipse_xy, fill='#fff', outline=None)

    image.save(f'dots_{iteration}.png')


