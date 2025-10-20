from flask import Flask, render_template, request, redirect, session
import csv
from werkzeug.security import check_password_hash
app = Flask(__name__)
app.secret_key = 'supersecretkey'

def load_users():
    users = {}
    try:
        with open('data/users.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    users[row[0]] = row[1]
    except FileNotFoundError:
        pass
    return users

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = load_users()
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users[username], password):
            session['user'] = username
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Credenziali non valide')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return render_template('dashboard.html', user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run()
