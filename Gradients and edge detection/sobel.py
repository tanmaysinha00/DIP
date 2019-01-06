import cv2
import numpy as np
img=cv2.imread("/home/saujanya/OCR/practice/test_images/coins.jpg")
cv2.imshow("Original",img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(img,cv2.CV_64F,0,1)
sobelX=np.uint8(np.absolute(sobelX))
sobelY=np.uint8(np.absolute(sobelY))
sobelC=cv2.bitwise_or(sobelX,sobelY)
cv2.imshow("sobelX",sobelX)
cv2.imshow("sobelY",sobelY)
cv2.imshow("sobelC",sobelC)
cv2.waitKey(0)
cv2.destroyAllWindows()