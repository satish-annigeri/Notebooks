from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Home Page"

@app.route('/hello')
@app.route('/hello/')
@app.route('/hello/<username>')
def hello_world(username='World'):
    return render_template('hello.html', username=username)

@app.route('/profile/')
@app.route('/profile')
@app.route('/profile/<username>')
def profile(username=None):
    if not username:
        return 'List of user Profiles'
    else:
        return 'Profile of user %s' % username

if __name__ == '__main__':
    app.run()

