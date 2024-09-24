from PIL import Image
import random

image_path_1 = "Brouwerij_florijn_element.png"  # Path to your first image
image_path_2 = "Brouwerij_florijn_element_2.png"  # Path to your second image
img1 = Image.open(image_path_1)
img2 = Image.open(image_path_2)

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

            # Randomly select one of the two images
            selected_img = random.choice([img1, img2])

            # Optional: Rotate the selected image randomly between 0 and 360 degrees
            rotated_img = selected_img.rotate(random.choice(rotations))  # Random rotation for each image

            # Paste the rotated image into the grid
            grid_img.paste(rotated_img, (x_offset, y_offset))

    # Show or save the final grid image
    grid_img.save(f"Brouwerij_florijn_img_{result_image}.png")
