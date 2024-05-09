import pandas as pd
from functions import *
from shapes import *
from gradients import *
from PIL import Image


if __name__ == "__main__":
    i = 0
    steps = 50
    for iteration in range(5):
        dataset = pd.read_csv('../data_sets/near_earth_objects.csv')

        df = pd.DataFrame(dataset)

        val1 = df['relative_velocity']
        val2 = df['miss_distance']

        img_width = 3000
        img_height = 3000

        factor = int(img_height / 1000) * 2

        image = Image.new('RGB', (img_width, img_height))

        # Creates the gradient for the background
        start_color = convert_hex_to_rgb("#FC5C7D")
        end_color = convert_hex_to_rgb("#6A82FB")

        line_color = (255, 255, 255)

        width = factor

        create_horizontal_gradient(image, img_width, img_height, start_color, end_color)

        data_set = []

        for val in range(steps):
            x1 = linear_map(val1[i], min(val1), max(val1), 0, img_width*2)
            x2 = linear_map(val2[i], min(val2), max(val2), 0, img_height)
            
            x1 = int(x1)
            x2 = int(x2)
            
            data_set.append((x1, x2))

            i += 1


        draw_polygon_with_circles(image=image, circle_size=5.0, data_set=data_set, line_color=line_color, width=width, close=True)

        file_name = f'polygon_{iteration}.png'
        image.save(file_name)
        print(f'Saved {file_name}')