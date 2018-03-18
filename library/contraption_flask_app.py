"""Creates Flask/html interface
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index.html')
def index_2():
    return render_template('index.html')


@app.route('/individual.html')
def individual():
    return render_template("individual.html")


@app.route('/group.html')
def group():
    return render_template("group.html")


@app.route('/patterns.html')
def patterns():
    return render_template("patterns.html")
