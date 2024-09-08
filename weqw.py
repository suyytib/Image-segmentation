import cv2
import matplotlib.pyplot as plt
image = cv2.imread('1232.png', 0)  # 0表示以灰度模式读取图像
equ = cv2.equalizeHist(image)
# 显示原图像和均衡化后的图像
plt.subplot(121), plt.imshow(image, 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(equ, 'gray')
plt.title('Histogram Equalization'), plt.xticks([]), plt.yticks([])
plt.show()