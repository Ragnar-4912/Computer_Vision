# crop
import os

import cv2


img = cv2.imread(os.path.join('.', 'Images', 'player.jpg'))

print(img.shape)

cropped_img = img[30:280, 132:332]

cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)
