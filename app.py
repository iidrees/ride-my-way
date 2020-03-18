import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


import settings

app = Flask(__name__)

db = SQLAlchemy(app)


@app.route("/home")
def hello_world():
    return "Hello World"



@app.route("/profiles", methods=["GET", "POST"])
def create_rides():
    try:
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        ride_name = request.form.get("ride-name")

        return "this is the name of the rider {} {}, and their ride {}".format(first_name, last_name, ride_name)
    except Exception as e:
        return(str(e))




if __name__ == "__main__":
    app.run()