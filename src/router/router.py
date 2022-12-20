from src import app
from flask import Flask, render_template, request, redirect, url_for, session
from src.controllers.login import LoginController
import re, bcrypt

loginController = LoginController()

@app.route('/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        account = loginController.validateLogin(username)
        passwordValidate = account[2]
        if bcrypt.checkpw(password.encode(), passwordValidate.encode()):
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            print("Contraseña incorrecta")
            msg = 'Incorrect username/password!'

            
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)

@app.route('/alpha/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))

@app.route('/alpha/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        passwordNone = request.form['password']
        passwordNone = passwordNone.encode()
        sal = bcrypt.gensalt()

        password = bcrypt.hashpw(passwordNone, sal)

        email = request.form['email']

        account = loginController.validateAccount(email)
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            loginController.createAccount(username, password, email)
            msg = 'You have successfully registered!'

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)

@app.route('/alpha/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/alpha/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        idu = session['id']
        account = loginController.profileAccount(idu)
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/alpha/collection')
def collection():
    # Check if user is loggedin
    if 'loggedin' in session:
        idu = session['id']
        account = loginController.profileAccount(idu)
        # Show the profile page with account info
        return render_template('collection.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))