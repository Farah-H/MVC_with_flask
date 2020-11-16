from flask import Flask, jsonify, redirect, url_for

app = Flask(__name__)

students = [
    { 'id':0, 'title': 'Miss.', 'first_name':'Farah','last_name':'Hassan', 'course':'DevOps'}
]

# decorator - to create our api/url for user to access our data in the browser
@app.route('/') # localhost:5000 is default port for Flask
def home():
    return '<h1>This is a dream team of DevOps consultants celebrating a WOW moment!!!</h1>'

# This function runs when the URl/ API is accessed

# creating our own API to display data on the specific route/URL/End point / API]
@app.route('/api/v1/student/data', methods = ['GET'])
def customised_api():
    return jsonify(students) # transforms data into Json 

# simple page to greet user
@app.route('/welcome/')
def greet_user():
    return 'Welcome to the DevOps team.'



## find a user the module to redirect the user back to the welcome page
## if page is not found (404) redirect the user to a welcome page
# @app.route('/')
# def page_not_found():
#     return redirect("/Welcome/", code=404)

# redirecting to a page
@app.route('/login')
def login():
    return redirect('/welcome/')

# taking input, returning fstring
@app.route('/<username>/')
def welcome_user(username):
    return f'<h1>Welcome to the dream team of DevOps {username}</h1>'

if __name__ == 'main':
    app.run(debug=True)
