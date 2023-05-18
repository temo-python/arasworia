from flask import Flask, render_template,redirect, session
from flask import url_for, flash, message_flashed, request
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hello'
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")
@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.from["usarname"]
        session['user'] = user
        return redirect(url_for('user'))
    else:
        return render_template('login.html')
@app.route("user")
def user():
    if 'user' in session:
        name = session['user']
        return F"Hello, {name}"
    else:
        return redirect(url_for('login'))
@app.route('/get_out')
def get_out():
    session.pop('username', None)
    return 'you are out'
if __name__ == '__main__':
    app.run()
