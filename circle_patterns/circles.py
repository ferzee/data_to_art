from PIL import Image, ImageDraw
import random
import functions

for file in range(5):
    IMG_HEIGHT = 3000
    IMG_WIDTH = 3000
    BG_COLOR = functions.convert_hex_to_rgb('#164863')
    LINE_COLOR = functions.convert_hex_to_rgb('#427D9D')

    image = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), BG_COLOR)

    draw = ImageDraw.Draw(image)


    circle_pos = (random.choice([0, 3000]), random.choice([0, 3000]))

    for circle in range(20):
        circle_size = random.randint(10, 750) * 10

        circle_xy = (
            circle_pos[0] - circle_size / 2,
            circle_pos[1] - circle_size / 2,
            circle_pos[0] + circle_size / 2,
            circle_pos[1] + circle_size / 2
        )

        width = random.randint(1, 3) * 10

        if random.choice([True, False]):
            LINE_COLOR = functions.convert_hex_to_rgb('#427D9D')
        else:
            LINE_COLOR = functions.convert_hex_to_rgb('#9BBEC8')

        draw.ellipse(xy=circle_xy, fill=None, outline=LINE_COLOR, width=width)

        prob = random.randint(1, 10)
        if prob < 6:
            arc_pos = [random.randint(0, 360), random.randint(0, 360)]
            start_arc = min(arc_pos)
            end_arc = max(arc_pos)
            width = width * 3
            draw.arc(xy=circle_xy, start=start_arc, end=end_arc, fill=LINE_COLOR, width=width)

    size = 500

    circle_xy = (
        circle_pos[0] - size / 2,
        circle_pos[1] - size / 2,
        circle_pos[0] + size / 2,
        circle_pos[1] + size / 2
    )

    draw.ellipse(xy=circle_xy, fill=LINE_COLOR, outline=None, width=0)

    image.save(f'test_{file}.png')
