import cv2
import numpy as np
# from matplotlib import pyplot as plt

img = cv2.imread(r'F:/Image_Processing/zebra.jpg')

blurred = cv2.blur(img,(5,5))

cv2.imwrite(r"F:/Image_Processing/zebra_blur.jpg", blurred)

# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()
# C:\Users\user\opencv-image-preprocessing-master\images