from rembg import remove
from PIL import Image
import io

def remove_background(input_path, output_path):
    # Open the input image
    with open(input_path, "rb") as input_image:
        input_data = input_image.read()
    
    # Remove the background
    output_data = remove(input_data)
    
    # Save the output image
    with open(output_path, "wb") as output_image:
        output_image.write(output_data)

    # Optionally open the image using Pillow
    img = Image.open(io.BytesIO(output_data))
    img.show()


input_image_path = "assets/images/img1.jpg"  # Path to your input image
output_image_path = "Output/img1.jpg"  # Path to save the image without background
remove_background(input_image_path, output_image_path)
