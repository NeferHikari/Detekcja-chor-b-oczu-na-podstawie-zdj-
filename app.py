from flask import Flask, render_template, request
from secrets import token_hex

import azure_utils

app = Flask(__name__)
app.config['SECRET_KEY'] = token_hex()
# app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.post('/upload')
def post_upload():
    eye_scan_image = request.files['eye_scan_image'].read()
    prediction = azure_utils.get_prediction(eye_scan_image)
    return render_template("show_pred.html")

if __name__ == '__main__':
    app.run(debug=True)
