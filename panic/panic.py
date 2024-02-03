from PIL import Image, ImageDraw
import random

img_width = 3000
img_height = 3000


for file in range(5):
    image = Image.new("RGBA", (img_width, img_height), "black")
    draw = ImageDraw.Draw(image)
    for i in range(30):
        center_xy = (random.randint(0, img_width), random.randint(0, img_height))
        size = random.randint(int(img_width / 20), int(img_width / 10))

        add = 0

        for j in range(20):
            increment = 10
            x, y = center_xy


            x += add if random.choice([True, False]) else x
            y += add if random.choice([True, False]) else y

            bounding_box = (
                x - size,
                y - size,
                x + size,
                y + size
            )

            if random.choice([True, True, False]):
                color = None
                outline = '#fff'
            else:
                opacity = random.randint(1, 255)
                color = (255, 255, 255, opacity)
                outline = None

            draw.ellipse(xy=bounding_box, fill=color, outline=outline)
            add += increment


    for i in range(50):
        start = (random.randint(0, img_width), random.randint(0, img_height))
        end = (random.randint(0, img_width), random.randint(0, img_height))
        add = 0
        random_range = random.randint(5, 25)
        for j in range(random_range):
            increment = img_width / 300
            draw.line(xy=((start[0] + add, start[1]), (end[0] + add, end[1])), width=1, fill="#fff")
            add += increment


    for i in range(5):
        size = random.randint(500, 2500)
        center_xy = (random.randint(0, img_width), random.randint(0, img_height))
        x, y = center_xy
        add = 0
        increment = 10
        for j in range(50):
            coords = [
                (x - size, y - add),
                (x, y - size - add),
                (x + size, y - add),
                (x, y + size - add)
            ]
            draw.polygon(xy=coords, fill=None, outline='#FF0000', width=2)
            add += increment

    for i in range(100):
        size = random.randint(10, 50)
        center_xy = (random.randint(0, img_width), random.randint(0, img_height))
        x, y = center_xy
        coords = [
            (x - size, y),
            (x, y - size),
            (x + size, y),
            (x, y + size)
        ]
        if random.choice([True, False]):
            fill = None
            outline = '#fff'
        else:
            fill = '#fff'
            outline = None

        draw.polygon(xy=coords, fill=fill, outline=outline, width=1)

        if not fill:
            add = 0
            increment = 5
            directions = ['left', 'right', 'up', 'down']

            for j in range(100):
                direction = random.choice(directions)
                if direction == 'up' or direction == 'down':
                    if direction == 'up':
                        add += increment
                    else:
                        add -= increment

                    coords = [
                        (x - size, y + add),
                        (x, y - size + add),
                        (x + size, y + add),
                        (x, y + size + add)
                    ]
                else:
                    if direction == 'left':
                        add += increment
                    else:
                        add -= increment

                    coords = [
                        (x - size + add, y),
                        (x + add, y - size),
                        (x + size + add, y),
                        (x + add, y + size)
                    ]

                draw.polygon(xy=coords, fill=fill, outline=outline, width=1)

    image.save(f'chaos_{file}.png')