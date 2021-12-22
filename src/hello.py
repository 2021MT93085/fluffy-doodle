from flask import Flask
from flask import render_template
from flask import url_for
import datetime
#app = Flask(__name__)
app = Flask(__name__, template_folder='templates')

# Selects the page for which a function is to be defined. Right now there will only be one page in your website.

@app.route('/index')
@app.route('/')
@app.route('/index/')
def index():
    #return "<h1>Hello World!</h1>" \
    #       "\nThis is my introduction to Flask!" \
    #       "\nI can write a lot of things on this page.\nLet's get started!"
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


# The above function returns the HTML code to be displayed on the page



if __name__ == '__main__':

   app.run()