from flask import Flask

# App Object
app = Flask(__name__)

# Single Route
@app.route('/') # View to route "/"
def index():
        return "Hello World"