# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:54:08 2021

@author: User
"""

from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "<b><i><h1>Hey there!</h1>"
if __name__ == '__main__':
    app.run(host='localhost', port='5002',debug=True)