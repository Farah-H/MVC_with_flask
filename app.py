from flask import Flask, jsonify

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

if __name__ == 'main':
    app.run(debug=True)
