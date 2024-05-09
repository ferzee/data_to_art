from PIL import Image, ImageDraw
import random
import functions

for file in range(5):
    IMG_HEIGHT = 3000
    IMG_WIDTH = 3000
    MARGIN = 300

    BG_COLOR = functions.convert_hex_to_rgb('#8F53A1')
    LINE_COLOR = functions.convert_hex_to_rgb('#FFDB4F')

    image = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), BG_COLOR)

    draw = ImageDraw.Draw(image)

    steps = 10

    step_size = IMG_WIDTH / steps

    peak_size = 500

    start_peak = -500

    for line in range(steps * 2):
        random_min = random.randint(0, 100)
        random_max = random.randint(0, 50)
        peak_range = (start_peak + random_min, start_peak + peak_size - random_max)

        points = []

        y = -500

        random_width = random.randint(50, 120)

        for i in range(steps * 2):

            if i % 2 == 0:
                x = peak_range[0]
            else:
                x = peak_range[1]

            coords = (x, y)
            points.append(coords)
            y += step_size

            draw.line(points, fill=LINE_COLOR, width=random_width, joint="curve")

        start_peak += step_size * 1.5


    #image.show()

    image.save(f"random_easter_{file}.png")
