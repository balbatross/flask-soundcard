from cvideo import Video

def get_camera(ix):
    return Video(0).start()

def get_frame(camera):
    return camera.read()

def fmt_frame(frame):
    enc = cv2.imencode('jpg', frame)
    return b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + enc + b'\r\n'
