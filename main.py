from email import message
from flask import Flask, render_template, request, jsonify
import math


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/square')
def redirect_square():
    return render_template('square.html')

@app.route('/triangle')
def redirect_triangle():
    return render_template('triangle.html')

@app.route('/convert')
def redirect_convert():
    return render_template('convert.html')


@app.route('/square', methods=['POST'])
def square():
    response = {}
    data = request.get_json()
    if data.get('sqrnumber'):
        sqrnumber = int(data['sqrnumber'])
        response = {'status': 200, 'result': math.sqrt(sqrnumber), 'message': 'Success'}
    else:
        response = {'status': 500, 'result': 0, 'message': 'Error'}
    return jsonify(response)

@app.route('/triangle', methods=['POST'])
def triangle():
    response = {}
    data = request.get_json()
    a = int(data.get('a'))
    b = int(data.get('b'))
    if data.get('a', 'b'):
        response = {'status': 200, 'result': math.hypot(a,b), 'message': 'Success'}
    else:
        response = {'status': 500, 'result': 0, 'message': 'Error'}
    return jsonify(response)


@app.route('/convert', methods=['POST'])
def convert():
    response = {}
    data = request.get_json()
    if data.get('cvtnumber'):
        cvtnumber = int(data['cvtnumber'])
        if cvtnumber >= 80:
            message = "A"
        elif cvtnumber >= 70 and cvtnumber <= 79:
            message = "B"

        elif cvtnumber >= 60 and cvtnumber <= 69:
            message = "C"

        elif cvtnumber >= 50 and cvtnumber <= 59:
            message = "D"
         
        elif cvtnumber <= 50:
            message = "E"

        else:
            message = "Could not calculate grade."
        response = {'status': 200, 'result': cvtnumber, 'message': message}
    else:
        response = {'status': 500, 'result': 0, 'message': 'Error'}
    return jsonify(response)
