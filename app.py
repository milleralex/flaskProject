from flask import Flask, render_template, Response
from markupsafe import escape
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)


def gen_frames():
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/btn/<btn_name>')
def press_button(btn_name):  # put application's code here
    print(escape(btn_name))
    return ""

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
