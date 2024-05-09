import random
import pandas as pd
from functions import *
from shapes import *
from gradients import *
from PIL import Image


if __name__ == "__main__":
    for iteration in range(5):
        dataset = pd.read_csv('data_set.csv')

        df = pd.DataFrame(dataset)

        vals_co2 = df['Co2']
        vals_temp = df['temperature_change_from_co2']

        img_width = 3000
        img_height = 3000

        factor = img_width / 1000

        image = Image.new('RGB', (img_width, img_height))

        # Creates the gradient for the background
        start_color = (95, 44, 130)
        end_color = (73, 160, 157)

        create_horizontal_gradient(image, img_width, img_height, start_color, end_color)

        for i in range(len(vals_co2)):
            try:
                co2_val = vals_co2[i]
                size = linear_map(co2_val, min(vals_co2), max(vals_co2), 10 * factor, 100 * factor)
                size = round(size)
                
                temp_val = vals_temp[i]
                angle = linear_map(temp_val, min(vals_temp), max(vals_temp), 100, img_width)
                
                rand_x = random.randint(1, img_width)
                rand_y = random.randint(1, img_height)

                width = linear_map(co2_val, min(vals_co2), max(vals_co2), 2 * factor, 4 * factor)
                width = round(width)

                draw_hexagon(image=image, center_x=rand_x, center_y=rand_y, size=size, outline_color=(255, 255, 255), angle=angle, width=width)
            except ValueError as ve:
                pass

        file_name = f'gradient_{iteration}.png'
        image.save(file_name)
        print(f'Saved gradient_{iteration}.png')
