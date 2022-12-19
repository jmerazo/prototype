from src.connection.con_db import mysql

class LoginModel():
    def validateLogin(self, username):
        # Check if account exists using MySQL
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        # Fetch one record and return result
        account = cursor.fetchone()
        return account

    def validateAccount(self, email):
        # Check if account exists using MySQL
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM accounts WHERE email = %s', (email,))
        account = cursor.fetchone()
        return account
    
    def createAccount(self, username, password, email):
        # Account doesnt exists and the form data is valid, now insert new account into accounts table
        cursor = mysql.get_db().cursor()
        cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
        mysql.get_db().commit()
        cursor.close()
    
    def profileAccount(self, idu):
        # We need all the account info for the user so we can display it on the profile page
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (idu,))
        account = cursor.fetchone()
        return account