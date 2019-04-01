import cv2

def get_camera(ix):
    return cv2.VideoCapture(ix)

def get_frame(camera):
    return camera.read()

def fmt_frame(frame):
    enc = cv2.imencode('jpg', frame)
    return b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + enc + b'\r\n'
