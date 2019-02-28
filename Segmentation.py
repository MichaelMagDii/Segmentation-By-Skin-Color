import sys
import numpy
import cv2

im = cv2.imread(#'Read an Image Here like(Image.jpg))
cv2.imshow('''Name of Image''',im)
im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)

skin_ycrcb_mint = numpy.array((0, 133, 77))
skin_ycrcb_maxt = numpy.array((255, 173, 127))
skin_ycrcb = cv2.inRange(im_ycrcb, skin_ycrcb_mint, skin_ycrcb_maxt)
cv2.imshow('Photos/output2.jpg', skin_ycrcb) # Second image
_, contours, _= cv2.findContours(skin_ycrcb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for i, c in enumerate(contours):
    area = cv2.contourArea(c)
    if area > 1000:
        cv2.drawContours(im, contours, i, (255, 0, 0), 3)
cv2.imwrite('Photos/output3.jpg', im)
cv2.waitKey(0)