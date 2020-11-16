from flask import Flask, jsonify, redirect, url_for, render_template
import base.html
import index.html
# create an instance of our app
app = Flask(__name__)

students = [
    {"id": 0, "title": "Ms.", "first_name": "Farah", "last_name": "Hassan", "course": "DevOps"}
]


# decorator - to create our api/url for user to access our data in the browser
@app.route("/")  # localhost:5000 is default port for Flask
def home():
    return "<h1>This is a dream team of DevOps consultants celebrating a WOW moment!!!</h1> "

@app.route("/welcome/") #localhost:5000/welcome/
def greet_user():
    return redirect(for_url('greet_user'))

# This function runs when the URL/API is accessed

# Creating our own API to display data on the specific route/URL/End point/API
@app.route("/api/v1/student/data/", methods=["GET"])
# this will add this API/URL to  http://127.0.0.1:5000/api/v1/student/data
def customised_api():
    return jsonify(students)  # transforms data into Json
    # Utilising Extract Transform Load

@app.route("/login/")
def login():
    return redirect(url_for("greet_user"))

@app.route("/<username>/")
def welcome_user(username):
    return f"<h1> Welcome to the dream team of DevOps dear {username}</h1>"

@app.route("/index/")
def index():
    return render_template("base.html")

@app.route('/child/')
def child():
    return render_template('index.html')

# @app.route('/child/')
# def to_ten():
#     for i in range (10):
#         return jsonify.i
@app.route('/loop')
def for_loop():
    return redirect(url_for("for_loop"))


if __name__ == "__main__":
    app.run(debug=True)