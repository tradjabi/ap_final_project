import cv2
# load the image and show it
image = cv2.imread("F:/Image_Processing/zebra.jpg")
# cv2.imshow("original", image)
# cv2.waitKey(0)
cropped = image[200:500, 200:500]
# cv2.imshow("cropped", cropped)
# cv2.waitKey(0)

cv2.imwrite("F:/Image_Processing/zebra_crop.jpg", cropped)








