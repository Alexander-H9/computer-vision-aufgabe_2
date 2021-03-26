import numpy as np
import cv2 as cv

img = cv.imread("barcode2.jpg")
windowName = "Barcode"

kernel = np.ones((3,3),np.uint8)    # 3x3 matrix with ones for the convolution. Easy explanation for kernels: https://towardsdatascience.com/basics-of-kernels-and-convolutions-with-opencv-c15311ab8f55
print("Kernel shape:\n", kernel)

while True:

    cv.imshow(windowName, img)

    k = cv.waitKey(1) & 0xFF

    if k == ord('q'):
        break

    elif k == ord('x'):
        print("horizontale kanten")

    elif k == ord('y'):
        print("vertikale kanten")

    elif k == ord('a'):
        print("glaetten")

    elif k == ord('t'):
        print("threshold")
        img_grey = cv.imread("barcode2.jpg", 0) # recommended is to use a grayscale image
        ret, thrashold = cv.threshold(img_grey, 126, 255, cv.THRESH_BINARY)   # https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html
        cv.imshow("Threshold", thrashold) 

    elif k == ord('e'):
        print("erode")
        erosion = cv.erode(img,kernel, iterations = 1)
        cv.imshow("Erode", erosion)

    elif k == ord('d'):
        print("dilate")
        dilation = cv.dilate(img,kernel, iterations = 1)
        cv.imshow("Dilate", dilation)

cv.destroyAllWindows()