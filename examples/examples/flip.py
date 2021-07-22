import cv2
import numpy as np

img = cv2.imread("F:/Image_Processing/babr.jpg")
print(type(img))
# <class 'numpy.ndarray'>

print(img.shape)
# (225, 400, 3)

# img_flip_ud = cv2.flip(img, 0)
# cv2.imwrite('data/dst/lena_cv_flip_ud.jpg', img_flip_ud)
# # True

img_flip_lr = cv2.flip(img, 1)
cv2.imwrite("F:/Image_Processing/babr_flip.jpg", img_flip_lr)
# True

