from shapes import *
from gradients import *
from PIL import Image
from random import randint

if __name__ == "__main__":

    steps = 10

    i = 0
    for iteration in range(5):

        img_width = 3000
        img_height = 3000

        margin_horizontal = img_width / 20
        margin_vertical = img_height / 20

        image = Image.new('RGB', (img_width, img_height))

        # Creates the gradient for the background
        start_color = convert_hex_to_rgb('#DBDBDB')
        end_color = convert_hex_to_rgb('#EAEAEA')

        line_color = convert_hex_to_rgb('#ADA996')
        line_width = 20

        create_vertical_gradient(image, img_width, img_height, start_color, end_color)

        data_set = []

        for val in range(steps):
            x1 = randint(int(margin_horizontal), int((img_width - margin_horizontal)))
            x2 = randint(int(margin_vertical), int((img_width - margin_vertical)))

            data_set.append((x1, x2))

        draw_polygon_with_rounded_edges(image=image, data_set=data_set, line_color=line_color, line_width=line_width, close=False, rounded=True)

        file_name = f'chique_{iteration}.png'
        image.save(file_name)
        print(f'Saved {file_name}')
        i += 1
