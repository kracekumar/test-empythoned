#! /usr/bin/env python

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


app.run('0.0.0.0', debug=True)
