from PIL import Image
from functions import convert_hex_to_rgb
from gradients import create_horizontal_gradient
import random


def place_image_on_canvas(canvas, canvas_size, image_path, max_angle=360):
    img = Image.open(image_path).convert("RGBA")

    # Randomly generate position within the canvas
    x = random.randint(-500, canvas_size)
    y = random.randint(-500, canvas_size)

    # Randomly generate rotation angle
    angle = random.randint(0, max_angle)

    # Rotate the image
    rotated_image = img.rotate(angle, expand=True)

    # Paste the rotated image onto the canvas
    canvas.paste(rotated_image, (x, y), rotated_image)


if __name__ == "__main__":

    img_size = 3000

    for file in range(5):
        image = Image.new("RGBA", (img_size, img_size), (255, 255, 255, 0))

        # Create image background with gradient
        start_color = convert_hex_to_rgb('#8f2323')
        end_color = convert_hex_to_rgb('#cc9d3a')
        create_horizontal_gradient(image, img_size, img_size, start_color, end_color)

        # Tweak
        max_triangles = 100

        for i in range(max_triangles):
            rand_num = random.randint(1, 6)
            path = f"gradient_triangles/triangle_{rand_num}.png"
            place_image_on_canvas(image, img_size, path)

        image.save(f"output_canvas_{file}.png")
        image.show()
