import numpy as np
import cv2 as cv

img = cv.imread("barcode2.jpg")
windowName = "Barcode"

kernel = img.Mat.ones(2,2)

cv.filter2D()



while True:

    cv.imshow(windowName, img)

    if cv.waitKey(1) == ord('q'):
        break

    elif cv.waitKey(1) == ord('x'):
        pass

    elif cv.waitKey(1) == ord('y'):
        pass

    elif cv.waitKey(1) == ord('a'):
        pass

    elif cv.waitKey(1) == ord('t'):
        pass

    elif cv.waitKey(1) == ord('e'):
        pass

    elif cv.waitKey(1) == ord('d'):
        pass