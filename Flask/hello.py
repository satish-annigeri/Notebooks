from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Home Page"

@app.route('/hello')
def hello_world():
    return 'Hello, World from Python Flask 0.10.1'

if __name__ == '__main__':
    app.run()

