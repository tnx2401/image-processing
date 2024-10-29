from PIL import Image
import cv2
import numpy as np
import os

def do_convolution(source_image, kernel):
    """Apply convolution to the source image using the given kernel."""
    destination_image = cv2.filter2D(source_image, -1, kernel, borderType=cv2.BORDER_DEFAULT)
    return destination_image

# Define paths
img_folder = 'C:/Users/Admin/OneDrive/Desktop/XLA/img'
output_folder = 'C:/Users/Admin/OneDrive/Desktop/XLA/output'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Define convolution kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]], dtype=np.float32)

# Process each image
for filename in os.listdir(img_folder):
    file_path = os.path.join(img_folder, filename)
    
    # Check if file is a gif
    if filename.lower().endswith('.gif'):
        try:
            # Open gif with PIL
            pil_img = Image.open(file_path).convert('L')
            source_image = np.array(pil_img)
        except Exception as e:
            print(f"Error reading gif: {filename}, {e}")
            continue
    else:
        # Open with OpenCV for other formats
        source_image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

    if source_image is None:
        print(f"Could not read the image: {filename}")
        continue
    
    # Perform convolution
    destination_image = do_convolution(source_image, kernel)

    # Combine and save the images as before
    combined_image = np.hstack((source_image, destination_image))
    output_path = os.path.join(output_folder, f"combined_{filename}.bmp")
    cv2.imwrite(output_path, combined_image)

    print(f"Saved combined image to {output_path}")

print("Convolution completed for all images.")
