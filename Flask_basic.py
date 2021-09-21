# GET, POST, PATCH, PUT

# HTTP status codes are made up of 3 digits that fall into 5 categories, with each category representing a certain class of code.
#
# The first digit is the category and the 5 categories correspond to the following class:
#
# 1xx - Informational
# 2xx - Success
# 3xx - Redirection
# 4xx - Client errors
# 5xx - Server errors
# The example of the "404 not found" status code falls under the "client error" category,
# where the client tried to request something that doesn't exist on the server.

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1> Hello World </h1>'

# DYNAMIC ROUTE
# http:127.0.0.5000/user/name
# hello piyush

@app.route('/user/<name>')
def user(name):
    return 'Hello, %s' % name

# headers

@app.route("/headers")
def headers():
   browser = request.headers.get('User-Agent')
   return '<p>Your Browser is %s</p>'% browser



if __name__ == '__main__':
    app.run(debug=True)


