"""Creates Flask/html interface
switch between mocpi and raspi
"""

from flask import Flask, render_template, request
#from library.mocpi import contraption
from library.raspi import contraption


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
        print("You posted to individual.html")
        print(request.form)
        led_number = request.form["led_number"]
        print(led_number)
        ledcon.led_on(int(led_number))
    elif request.method == 'GET':
        print("Here's 'Individual' web-page")
    return render_template("individual.html")


@app.route('/group.html', methods=['GET', 'POST'])
def group():
    if request.method == 'POST':
        print("You posted to group.html")
        print(request.form)

        #LED 0
        if 'on' == request.form['led_number0']:
            print(request.form['led_number0'])
            print("flask: led 0 is on")
            ledcon.led_on(0)
        else:
            print("flask:Led 0 is off")
            ledcon.led_off(0)


        #LED 1
        if request.form['led_number1'] == 'on':
            print("flask: led 1 is on")
            ledcon.led_on(1)

        else:
            print("flask:Led 1 is off")
            ledcon.led_off(1)

        #LED 2
        if request.form['led_number2'] == 'on':
            print("flask: led 2 is on")
            ledcon.led_on(2)
        else:
            print("flask:Led 2 is off")
            ledcon.led_off(2)

        #LED 3
        if request.form['led_number3'] == 'on':
            ledcon.led_on(3)
        else:
            ledcon.led_off(3)

        #LED 4
        if request.form['led_number4'] == 'on':
            ledcon.led_on(4)
        else:
            ledcon.led_off(4)

        #LED 5
        if request.form['led_number5'] == 'on':
            ledcon.led_on(5)
        else:
            ledcon.led_off(5)

        #LED 6
        if request.form['led_number6'] == 'on':
            ledcon.led_on(6)
        else:
            ledcon.led_off(6)

        #LED 7
        if request.form['led_number7'] == 'on':
            ledcon.led_on(7)
        else:
            ledcon.led_off(7)

        #LED 8
        if request.form['led_number8'] == 'on':
            ledcon.led_on(8)
        else:
            ledcon.led_off(8)

        #LED 9
        if request.form['led_number9'] == 'on':
            ledcon.led_on(9)
        else:
            ledcon.led_off(9)

    elif request.method == 'GET':
        print("Here's 'Group' web-page")

    return render_template("group.html")


@app.route('/patterns.html', methods=['GET', 'POST'])
def patterns():
    if request.method == 'POST':
        print("You posted to patterns.html")
        print(request.form)
        p=request.form['pattern']
        '''A nice way to improve debugability'''
        print(p)
        if request.form['pattern'] == 'Race Up':
            print("flask race up")
            ledcon.race_up()
        elif request.form['pattern'] == 'Race Down':
            print("flask: race down")
            ledcon.race_down()
        elif request.form['pattern'] == 'Dance!':
            print("flask: dancing")
            ledcon.dance()
    elif request.method == 'GET':
        print("Here's 'Patterns' web-page")
    return render_template("patterns.html")

