import cv2
import numpy as np
import pickle

def build_squares(img):
    x, y, w, h = 420, 140, 10, 10
    d = 10
    imgCrop = None
    crop = None
    for i in range(10):
        for j in range(5):
            if imgCrop is None:
                imgCrop = img[y:y+h, x:x+w]
            else:
                imgCrop = np.hstack((imgCrop, img[y:y+h, x:x+w]))
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
            x += w + d
        if crop is None:
            crop = imgCrop
        else:
            crop = np.vstack((crop, imgCrop))
        imgCrop = None
        x = 420
        y += h + d
    return crop

def get_hand_hist():
    cam = cv2.VideoCapture(1)
    if not cam.read()[0]:
        cam = cv2.VideoCapture(0)
    
    flagPressedC, flagPressedS = False, False
    imgCrop = None
    
    while True:
        ret, img = cam.read()
        if not ret:
            break
        img = cv2.flip(img, 1)
        img = cv2.resize(img, (640, 480))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        keypress = cv2.waitKey(1)
        if keypress == ord('c'):
            hsvCrop = cv2.cvtColor(imgCrop, cv2.COLOR_BGR2HSV)
            flagPressedC = True
            hist = cv2.calcHist([hsvCrop], [0, 1], None, [180, 256], [0, 180, 0, 256])
            cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
        
        elif keypress == ord('s'):
            flagPressedS = True
            break
        elif keypress == ord('x'):
            break

        if flagPressedC:
            dst = cv2.calcBackProject([hsv], [0, 1], hist, [0, 180, 0, 256], 1)
            #convolution with a circular disc
            disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
            cv2.filter2D(dst, -1, disc, dst)
            
            # Blur
            blur = cv2.GaussianBlur(dst, (11, 11), 0)
            blur = cv2.medianBlur(blur, 15)

            ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            kernel = np.ones((5, 5), np.uint8)
            thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
            thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

            #for ulta krn ke luye
            thresh = cv2.bitwise_not(thresh)

            thresh = cv2.merge((thresh, thresh, thresh))
            cv2.imshow("Thresh", thresh)
        
        if not flagPressedS:
            imgCrop = build_squares(img)

        cv2.imshow("Set hand histogram", img)
    
    cam.release()
    cv2.destroyAllWindows()
    
    with open("hist", "wb") as f:
        pickle.dump(hist, f)

get_hand_hist()

