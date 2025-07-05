
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded credentials
USERNAME = 'admin'
PASSWORD = 'password123'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USERNAME and password == PASSWORD:
            return redirect(url_for('welcome', username=username))
        else:
            return redirect(url_for('error'))
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    username = request.args.get('username', 'User')
    return render_template('welcome.html', username=username)

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
