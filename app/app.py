#!/usr/bin/python

from flask import Flask
from waitress import serve
app = Flask(__name__)

@app.route('/')
def home():
    return "Success!"

@app.route('/ping')
def ping():
    return "Ok"

if __name__ == '__main__':
    serve(app)