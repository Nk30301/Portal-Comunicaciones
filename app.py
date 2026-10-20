import os

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

VIDEO_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'video')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/video/<path:filename>')
def video(filename):
    return send_from_directory(VIDEO_FOLDER, filename)

if __name__ == '__main__':
    # Se ejecuta en el puerto 5000 en modo depuración
    app.run(debug=True, host='0.0.0.0', port=9000)
