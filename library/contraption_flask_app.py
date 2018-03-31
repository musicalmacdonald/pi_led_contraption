"""Creates Flask/html interface
"""

from flask import Flask, render_template, request
from library.mocpi import contraption


app = Flask(__name__)

ledcon = contraption.PiLedContraption()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index.html')
def index_2():
    return render_template('index.html')


@app.route('/individual.html', methods=['GET', 'POST'])
def individual():
    if request.method == 'POST':
        print("You posted")
        print(request.form)
        led_number = request.form["led_number"]
        print(led_number)
        ledcon.led_on(int(led_number))
    elif request.method == 'GET':
        print("Here's your web-page")
    return render_template("individual.html")


@app.route('/group.html')
def group():
    return render_template("group.html")


@app.route('/patterns.html')
def patterns():
    return render_template("patterns.html")

