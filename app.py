import os

from flask import Flask, request, jsonify

import settings

app = Flask(__name__)

@app.route("/home")
def hello_world():
    return "Hello World"



if __name__ == "__main__":
    app.run()