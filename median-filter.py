import cv2
import numpy as np
import random

# Function to add salt-and-pepper noise to an image
def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = image.copy()
    num_salt = int(salt_prob * image.size)
    num_pepper = int(pepper_prob * image.size)

    # Add salt (white) noise
    for _ in range(num_salt):
        i = random.randint(0, image.shape[0] - 1)
        j = random.randint(0, image.shape[1] - 1)
        noisy_image[i, j] = 255

    # Add pepper (black) noise
    for _ in range(num_pepper):
        i = random.randint(0, image.shape[0] - 1)
        j = random.randint(0, image.shape[1] - 1)
        noisy_image[i, j] = 0

    return noisy_image

# Read input image
img = cv2.imread('./img/1.bmp', cv2.IMREAD_GRAYSCALE)

# Add salt-and-pepper noise to the image
salt_prob = 0.02  # Probability of salt noise
pepper_prob = 0.02  # Probability of pepper noise
noisy_img = add_salt_and_pepper_noise(img, salt_prob, pepper_prob)

# Apply median filter with a 3x3 kernel
median_filtered_img = cv2.medianBlur(noisy_img, 3)

# Display original, noisy, and filtered images
cv2.imshow("Original Image", img)
cv2.imshow("Noisy Image", noisy_img)
cv2.imshow("Median Filtered Image", median_filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
