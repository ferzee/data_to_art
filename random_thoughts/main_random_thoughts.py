from shapes import *
from gradients import *
from PIL import Image
from random import randint

if __name__ == "__main__":

    gradients = {
        'Witching Hour': ['#c31432', '#240b36'],
        'Ultra Violet': ['#654ea3', '#eaafc8'],
        'Blue Raspberry': ['#00B4DB', '#0083B0'],
        'Slight Ocean View': ['#a8c0ff', '#3f2b96'],
        'Ohhappiness': ['#00b09b', '#96c93d']
    }

    indexed_gradients = list(gradients.items())

    steps = 40

    i = 0
    for iteration in range(5):

        img_width = 3000
        img_height = 3000

        margin_horizontal = img_width / 20
        margin_vertical = img_height / 20

        image = Image.new('RGB', (img_width, img_height))

        # Creates the gradient for the background
        start_color = convert_hex_to_rgb(indexed_gradients[i][1][0])
        end_color = convert_hex_to_rgb(indexed_gradients[i][1][1])

        line_color = (255, 255, 255)

        create_vertical_gradient(image, img_width, img_height, start_color, end_color)

        data_set = []

        for val in range(steps):
            x1 = randint(int(margin_horizontal), int((img_width - margin_horizontal)))
            x2 = randint(int(margin_vertical), int((img_width - margin_vertical)))

            data_set.append((x1, x2))

        circle_width = 50
        draw_polygon_with_circles(image=image, width=10, circle_size=circle_width, data_set=data_set, line_color=line_color, close=True)

        file_name = f'polygon_{iteration}.png'
        image.save(file_name)
        print(f'Saved {file_name}')
        i += 1
