import cv2

image = cv2.imread("D:/PROJECTS/Python-Projects/Image Resizer/sample2.jpg", cv2.IMREAD_UNCHANGED)

# cv2.imshow("Image", image)

# Resizing the image
scale_percentage = 100

#calculate the 50 percent of original dimensions
width = int(image.shape[1] * scale_percentage / 100)
height = int(image.shape[0] * scale_percentage / 100)

# dsize
dsize = (width, height)

# resize image
output = cv2.resize(image, dsize)

cv2.imwrite("resized_image.jpg", output)
cv2.imshow("Resized image", output)
cv2.waitKey(0)
