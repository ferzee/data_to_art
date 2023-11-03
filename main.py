import pandas as pd
from functions import *
from shapes import *
from gradients import *
from PIL import Image

if __name__ == "__main__":
    dataset = pd.read_csv('housing/housing.csv')

    df = pd.DataFrame(dataset)

    val1 = df['buy']
    val2 = df['sell']

    img_width = 3000
    img_height = 3000

    margin = img_width / 10

    circle_size = int(img_width / 4)

    image = Image.new('RGB', (img_width, img_height))

    # Creates the gradient for the background
    start_color = convert_hex_to_rgb("#649173")
    end_color = convert_hex_to_rgb("#DBD5A4")

    line_color = (255, 255, 255)

    create_horizontal_gradient(image, img_width, img_height, start_color, end_color)

    for i in range(len(val1)):
        x = linear_map(val1[i], min(val1), max(val1), margin, img_width - margin)
        y = linear_map(val2[i], min(val2), max(val2), margin, img_height - margin)

        x = int(x)
        y = int(y)

        draw_hexagon(
            center_x=x,
            center_y=y,
            size=circle_size,
            outline_color=line_color,
            angle=0.0,
            width=10,
            image=image
        )

    file_name = f'housing.png'
    image.save(file_name)
    print(f'Saved {file_name}')
