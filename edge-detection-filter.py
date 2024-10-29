import cv2
import numpy as np

# Đọc ảnh đầu vào ở chế độ grayscale
img = cv2.imread('./img/2.bmp', cv2.IMREAD_GRAYSCALE)

# Áp dụng bộ lọc Sobel theo hướng x (đường viền ngang)
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

# Áp dụng bộ lọc Sobel theo hướng y (đường viền dọc)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

# Kết hợp hai đường viền
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Chuyển đổi về kiểu uint8
sobel_combined = cv2.convertScaleAbs(sobel_combined)

# Hiển thị ảnh gốc và ảnh đã lọc Sobel
cv2.imshow("Original Image", img)
cv2.imshow("Sobel Filtered Image", sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
