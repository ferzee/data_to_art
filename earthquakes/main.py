import random
import pandas as pd
from functions import *
from shapes import *
from gradients import *
from PIL import Image

width = 3000
height = 3000
margin = 500

start_color = convert_hex_to_rgb('#093028')
end_color = convert_hex_to_rgb('#237A57')

image = Image.new("RGB", (width, height))
create_vertical_gradient(image, width, height, start_color, end_color)

if __name__ == "__main__":
    dataset = pd.read_csv('Earthquake.csv')

    coords_x = []
    coords_y = []
    magnitudes = []

    df = pd.DataFrame(dataset)

    for latitude in df['Latitude']:
        x = linear_map(latitude, min(df['Latitude']), max(df['Latitude']), 150, width - margin)
        coords_x.append(x)

    for longitude in df['Longitude']:
        y = linear_map(longitude, min(df['Longitude']), max(df['Longitude']), margin, height - 600)
        coords_y.append(y)

    for mag in df['Magnitude']:
        mag = linear_map(mag, min(df['Magnitude']), max(df['Magnitude']), 100, 1000)
        magnitudes.append(mag)

    i = 0

    for val in coords_x:
        draw = ImageDraw.Draw(image)

        circle_width = magnitudes[i]

        draw.ellipse((
            (coords_x[i]-circle_width/2, coords_y[i]-circle_width/2),
            (coords_x[i] + circle_width/2, coords_y[i] + circle_width/2)),
            fill=None, outline=(255, 255, 255), width=3)
        i += 1

    image.save('earthquake_data.png')

