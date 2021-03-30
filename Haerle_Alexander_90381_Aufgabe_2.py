import numpy as np
import cv2 as cv

img = cv.imread("barcode2.jpg")
imgP = cv.imread("pirates1.jpg")
windowName = "Barcode"

kernel = np.ones((5, 5),np.uint8)    # 3x3 matrix with ones for the convolution. Easy explanation for kernels: https://towardsdatascience.com/basics-of-kernels-and-convolutions-with-opencv-c15311ab8f55
print("Kernel shape:\n", kernel)

gauss_kernel = np.array([[1,2,1], [2,4,2], [1,2,1]], np.uint8)/16 # zum glätten geeignet
print("Gauß-Kernel shape:\n", gauss_kernel)

horizontal_kernel = np.array([[3,0,-3], [10,0,-10], [3,0,-3]])
vertikal_kernel = np.array([[3,10,3], [0,0,0], [-3,-10,-3]])

def blur(working_img, working_kernel):
    return cv.filter2D(working_img, -1, working_kernel)


while True:

    cv.imshow(windowName, img)

    k = cv.waitKey(1) & 0xFF

    if k == ord('q'):
        break

    elif k == ord('x'):
        print("horizontale kanten")
        # Wenn man Ableitungs Filter benutzt ist es wichtig zuerst das Signal zu glätten
        blurred = blur(img, gauss_kernel)
        horizontal = cv.filter2D(blurred, -1 , horizontal_kernel)
        cv.imshow("Horizontale Kantenhervorhebung" , horizontal)

    elif k == ord('y'):
        print("vertikale kanten")
        # Wenn man Ableitungs Filter benutzt ist es wichtig zuerst das Signal zu glätten
        blurred = blur(img, gauss_kernel)
        vertikal = cv.filter2D(blurred, -1 , vertikal_kernel)
        cv.imshow("Vertikale Kantenhervorhebung" , vertikal)

    elif k == ord('a'):
        print("glaetten")
        glatt = blur(img, gauss_kernel)
        cv.imshow("Geglaettet", glatt)

    elif k == ord('t'):
        print("threshold")
        img_grey = cv.imread("barcode2.jpg", 0) # recommended is to use a grayscale image
        ret, thrashold = cv.threshold(img_grey, 126, 255, cv.THRESH_BINARY)   # https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html
        cv.imshow("Threshold", thrashold) 

    elif k == ord('e'):
        print("erode")
        erosion = cv.erode(img, kernel, iterations = 1)
        cv.imshow("Erode", erosion)

    elif k == ord('d'):
        print("dilate")
        dilation = cv.dilate(img, kernel, iterations = 1)
        cv.imshow("Dilate", dilation)

cv.destroyAllWindows()