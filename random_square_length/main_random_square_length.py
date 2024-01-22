from PIL import Image, ImageDraw
import random


def random_partition(length, num_parts):
    # Generate random partition lengths
    partitions = [random.uniform(0, length) for _ in range(num_parts)]

    # Normalize the partition lengths to sum up to the original length
    total = sum(partitions)
    partitions = [length * x / total for x in partitions]

    return partitions



IMG_HEIGHT = 3000
IMG_WIDTH = 3000
BG_COLOR = '#FFF'
COLORS = [
    "#F18674",
    "#F9D2A9",
    "#5B9B81",
    "#63AAA6"
]

for file in range(5):
    image = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(image)
    parts = random.randint(8, 20)

    x = 0

    parts_width = 20

    for i in range(parts_width):
        lengths = random_partition(IMG_HEIGHT, parts)
        y = 0

        width = IMG_WIDTH / parts_width

        for leng in lengths:
            draw.rectangle(xy=((x, y), (x + width, y + leng)), fill=random.choice(COLORS), outline=None, width=0)
            y += leng
        x += width


    image.save(f"random_square_length{file}.png")
