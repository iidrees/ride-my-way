import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

import settings
# from config import Config

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 


db = SQLAlchemy(app)

from api.models.user import User


@app.route("/home")
def hello_world():
    user = User.query.filter().all()
    print(user[0:])
    return "Hello World {}".format(user[:])


@app.route("/signup", methods=["POST"])
def sign_up():
    try:
        # print(request)
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        ride_name = request.form.get("username")

        user = User(
            first_name=first_name,
            last_name=last_name,
            username=ride_name
        )

        db.session.add(user)
        db.session.commit()
        return "this is the name of the rider {} {}, and their ride {}".format(first_name, last_name, ride_name)
    except Exception as e:
        return(str(e))
    

@app.route("/profiles", methods=["GET", "POST","DELETE"])
def create_rides():
    if request.method == "POST": 
        try:
            # print(request.form.get)
            first_name = request.form.get("first-name")
            last_name = request.form.get("last-name")
            ride_name = request.form.get("ride-name")
            user = User(
                first_name=first_name,
                last_name=last_name,
                username=ride_name
            )

            db.session.add(user)
            db.session.commit()
            return "this is the name of the rider {} {}, and their ride {}".format(first_name, last_name, ride_name)
        except Exception as e:
            return(str(e))
    elif request.method == "DELETE":
        first_name = request.form.get("first-name")
        print(first_name)
        try:
            user = User.query.filter_by(username="abd").first()
            print(">>>>>>>>",user)
            db.session.delete(user)
            db.session.commit()
            return "User has been deleted"
        except Exception as e:
            return(str(e))




if __name__ == "__main__":
    app.run()