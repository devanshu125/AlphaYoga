import cv2
import predict

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
        self.preds = None
        self.current_exercise = None 

    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        self.preds = predict.run(image)
        # print("predicton": self.preds)

        image_preds = image.copy()
        image_no = image.copy()

        print(self.current_exercise, self.preds)

        if self.current_exercise == self.preds:
            text = self.preds
        else:
            text = "Detecting..."

        _h, _w, _c = image_preds.shape
        cv2.putText(image_preds, text, (_h//2+2,_w//2+2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2, cv2.LINE_AA)
        ret, jpeg_preds = cv2.imencode('.jpg', image_preds)

        # _h, _w, _c = image_no.shape
        # cv2.putText(image_no, "detecting...", (_h//2+2,_w//2+2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2, cv2.LINE_AA)
        # ret, jpeg_no = cv2.imencode('.jpg', image_no)



        return jpeg_preds, jpeg_preds.tobytes(), self.preds