import cv2
# load the image and show it
image = cv2.imread("F:/Image_Processing/zebra.jpg")
# cv2.imshow("original", image)
# cv2.waitKey(0)

(h, w) = image.shape[:2]
center = (w / 2, h / 2)
# rotate the image by 180 degrees
M = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
# cv2.imshow("rotated", rotated)
# cv2.waitKey(0)

cv2.imwrite("F:/Image_Processing/zebra_rotate.jpg", rotated)