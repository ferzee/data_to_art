from PIL import Image
import random

ampersand_tile = "tile_ampersand.png"
dot_tile = "tile_dot.png"
empty_tile = "empty_tile.png"
img1 = Image.open(ampersand_tile)
img2 = Image.open(dot_tile)
img3 = Image.open(empty_tile)

# Define the customizable grid dimensions (e.g., 100 wide, 20 high)
grid_width_count = 10  # Number of images horizontally
grid_height_count = 10  # Number of images vertically

# Get the image size
img_width, img_height = img1.size  # Assuming both images are of the same size

# Create a new blank image for the grid (canvas size: grid_size * image_size)
canvas_width = grid_width_count * img_width
canvas_height = grid_height_count * img_height
grid_img = Image.new('RGB', (canvas_width, canvas_height), color='white')  # You can change the background color

rotations = [0, 90, 180, 270]

for result_image in range(5):
    # Rotate the images and place them in the grid
    for i in range(grid_height_count):
        for j in range(grid_width_count):
            # Calculate position where the image will be pasted
            x_offset = j * img_width
            y_offset = i * img_height

            random_num = random.randint(0, 10)
            if random_num < 1:
                selected_img = img1

            else:
                random_num = random.randint(0, 10)
                if random_num < 1:
                    selected_img = img2.rotate(random.choice(rotations))
                else:
                    selected_img = img3

            grid_img.paste(selected_img, (x_offset, y_offset))

    # Show or save the final grid image
    # grid_img.show()
    grid_img.save(f"Ampersand_img_{result_image}.png")
