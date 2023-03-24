import cv2
import numpy as np
from django.conf import settings
import dlib
from fer import FER

def opencv_dlib(path):
    img = cv2.imread(path,1)
    h, w = img.shape[0], img.shape[1]
    #try:
    if(type(img) is np.ndarray):
        detector = FER()
        results=detector.detect_emotions(img)
        for i in range(len(results)):
            Keymax = max(results[i]['emotions'], key=results[i]['emotions'].get)
            bounding_box = results[i]["box"]
            cv2.rectangle(img, (bounding_box[0], bounding_box[1]),
                      (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]), (0, 155, 255), 2, )
            cv2.putText(img, f'{Keymax}', (int(bounding_box[0] / 3), int(h / 1.15)), cv2.FONT_HERSHEY_SIMPLEX, 2,
                    (255, 0, 0), 2)

        cv2.imwrite(path,img)

    else:
        print("Image error in opencv_dlib")
        print(path)
    #except:
        #cv2.putText(img, f'Face not recognised', (int(bounding_box[0] / 3), int(h / 1.15)), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
        #cv2.imwrite(path, img)
