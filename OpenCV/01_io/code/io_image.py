import os
import cv2

# read image
image_path = os.path.join('.', 'Images', 'car.jpg')
img = cv2.imread(image_path)

# write image
output_path = os.path.join('.', 'Images', 'car1_out.jpg')
cv2.imwrite(output_path, img)

# visualize image
cv2.imshow('image', img)
cv2.waitKey(0)

# Destroy the window after any key is pressed
cv2.destroyAllWindows()
