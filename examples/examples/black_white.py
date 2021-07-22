import cv2
import numpy as np

import cv2
im_gray = cv2.imread('F:/Image_Processing/zebra.jpg', cv2.IMREAD_GRAYSCALE)
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh = 127
im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('F:/Image_Processing/bw_image.jpg', im_bw)


