# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 16:49:59 2021

@author: css129482
"""

from flask import Flask

PORT = 8000
MESSAGE = "Hello, world!\n"

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
    