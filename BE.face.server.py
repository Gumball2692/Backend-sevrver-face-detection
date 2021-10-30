from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request

import numpy as np
import cv2
import base64


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def dem_so_mat(face):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 10)

    so_mat = len(faces)
    return so_mat

def chuyen_base64_sang_anh(base64_pic):
    try:
        base64_pic = np.fromstring(base64.b64decode(base64_pic), dtype=np.uint8)
        base64_pic = cv2.imdecode(base64_pic, cv2.IMREAD_ANYCOLOR)
    except:
        return None
    return base64_pic

@app.route('/nhandienkhuonmat', methods=['POST'])
@cross_origin(origin='*')
def nhandienkhuonmat_process():
    face_numbers = 0
    facebase64 = request.form.get('facebase64')
    face = chuyen_base64_sang_anh(facebase64)
    face_numbers = dem_so_mat(face)
    return "So mat la = " + str(face_numbers)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='2692')
