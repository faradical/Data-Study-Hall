# DENDENCIES
from pymongo import MongoClient as MC
from flask import Flask, jsonify, request, render_template
from bson import json_util
import json

# DEFINE FLASK APPLICATION
app = Flask(__name__)

# ESTABLISH BATABASE CONNECTION
client = MC()
#
#

# DEFINE WEB ROUTES

@app.route("/")
def home():
    return render_template("/index.html")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("/login/index.html")

    elif request.method == 'POST':
        data = request.form
        # Add username and password to database

        # Create authToken

        # Return authToken and redirect 

@app.route("/result1", methods=['GET','POST'])
def result1():
    if request.method == 'GET':
        form_data = {"fname": "none",
                     "lname": "none",
                     "age": "none"}
        return render_template("/result1/index.html", data=form_data)

    elif request.method == 'POST':
        form_data = request.form
        print(form_data)
        return render_template("/result1/index.html", data=form_data)

@app.route("/pet")
def pet():
    # DO STUFF
    return render_template("/pet/index.html")

@app.route("/pet/result2/<name>/<type>")
def result2(name="None",type="None"):

    # Seth's extra demo stuf

    # DO STUFF#
    title = "Pet Results"
    return render_template("/pet/result2/index.html", name=name, type=type, title=title)

@app.route("/model/<value1>/<value2>")
def result3(value1="None",value2="None"):
    def model_predict(v1, v2):
        return int(v1) * int(v2)

    my_big_dict = {'result': model_predict(value1, value2)}
    return jsonify(my_big_dict)

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)

    print(type(resp))
    resp.status_code = 404

    return resp







# @app.route("/api")
# def new_hero():
# 	# DO STUFF

# @app.route("/api/getValue/<>")
# def new_hero():
# 	# DO STUFF

# @app.route("/api/", methods=['POST'])
# def new_hero():
# 	data = request.get_json(force=True)

# @app.route("/api/", methods=['POST'])
# def new_hero():
# 	data = request.get_json(force=True)

if __name__ == "__main__":
    app.run(debug=True)