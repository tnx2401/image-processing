import cv2
import numpy as np

def add_gaussian_noise(image, mean=0, sigma=5):
    """Add Gaussian noise to an image."""
    noise = np.random.normal(mean, sigma, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    return noisy_image

# Read the input image in grayscale
img = cv2.imread('./img/2.bmp', cv2.IMREAD_GRAYSCALE)

# Add Gaussian noise to the original image
noisy_img = add_gaussian_noise(img)

# Apply Gaussian filter with a kernel size of 5x5
gaussian_filtered_img = cv2.GaussianBlur(noisy_img, (5, 5), 0)

# Display the original, noisy, and Gaussian filtered images
cv2.imshow("Noisy Image", noisy_img)
cv2.imshow("Gaussian Filtered Image", gaussian_filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
