import cv2
# load the image and show it
image = cv2.imread("F:/Image_Processing/zebra.jpg")
# cv2.imshow("original", image)
# cv2.waitKey(0)

# we need to keep in mind aspect ratio so the image does
# not look skewed or distorted -- therefore, we calculate
# the ratio of the new image to the old image
r = 100.0 / image.shape[1]
dim = (100, int(image.shape[0] * r))
# perform the actual resizing of the image and show it
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
# cv2.imshow("resized", resized)
# cv2.waitKey(0)

cv2.imwrite("F:/Image_Processing/zebra_resize.jpg", resized)