import cv2, urllib.request
import numpy as np
import imutils
from imutils.video import FPS
from imutils.video import VideoStream
from django.conf import settings
import dlib
from fer import FER

class VideoCamera(object):
    def __init__(self):
        print("Emotion Detection Constructor..")
        self.video = VideoStream(src=0).start()
        self.fps = FPS().start()
    
    def __del__(self):
        print("Emotion Detection Destructor..")
        self.video.stop()
        cv2.destroyAllWindows()
    
    # def get_frame(self):
    #     img = self.video.read()
    #     img = cv2.flip(img,1)
    #     img = imutils.resize(img, width=600, height=400)
    #     try:
    #         detector2 = dlib.get_frontal_face_detector()
    #         detector = FER()
    #         results=detector.detect_emotions(img)
    #         Keymax = max(results[0]['emotions'], key=results[0]['emotions'].get)
    #         detected = detector2(img, 1)
    #
    #         if len(detected) > 0:
    #             for i, d in enumerate(detected):
    #                 x1, y1, x2, y2, w, h = d.left(), d.top(), d.right() + 1, d.bottom() + 1, d.width(), d.height()
    #                 cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
    #                 img=cv2.resize(img,(600,600))
    #                 print(img.shape)
    #                 h,w=img.shape[0],img.shape[1]
    #         cv2.putText(img,f'{Keymax}',(int(x1/3),int(h/1.15)),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)
    #
    #         self.fps.update()
    #         ret, jpeg = cv2.imencode('.jpg', img)
    #         return jpeg.tobytes()
    #     except:
    #         ret, jpeg = cv2.imencode('.jpg', img)
    #         return jpeg.tobytes()

    def get_frame(self):
        img = self.video.read()
        img = cv2.flip(img,1)
        img = imutils.resize(img, width=600, height=400)
        h, w = img.shape[0], img.shape[1]
        try:
            detector = FER()
            results=detector.detect_emotions(img)
            bounding_box = results[0]["box"]
            Keymax = max(results[0]['emotions'], key=results[0]['emotions'].get)
            cv2.rectangle(img, (bounding_box[0], bounding_box[1]),
                          (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]), (0, 155, 255), 2, )
            cv2.putText(img, f'{Keymax}', (int(bounding_box[0] / 3), int(h / 1.15)), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)


            self.fps.update()
            ret, jpeg = cv2.imencode('.jpg', img)
            return jpeg.tobytes()
        except:
            ret, jpeg = cv2.imencode('.jpg', img)
            return jpeg.tobytes()
