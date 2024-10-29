import cv2
import numpy as np

# Đọc ảnh đầu vào
img = cv2.imread('./img/2.bmp', cv2.IMREAD_GRAYSCALE)

# Áp dụng lọc trung bình với kernel 3x3
mean_filtered_img = cv2.blur(img, (3, 3))

# Hiển thị ảnh gốc và ảnh sau khi lọc trung bình
cv2.imshow("Original Image", img)
cv2.imshow("Mean Filtered Image", mean_filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()