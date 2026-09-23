from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Se ejecuta en el puerto 5000 en modo depuración
    app.run(debug=True, host='0.0.0.0', port=9000)