from flask import Flask, Response, render_template
import cv2

app=Flask(__name__)

camera = cv2.VideoCapture(0)

@app.route('/video_feed')
def vid_feed() :
    return Response(gen_frames(), mimetype='multipat/x-mixed-replace; boundary=frame')

def gen_frames() :
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
