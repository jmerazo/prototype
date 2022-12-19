from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

# Enter your database connection details below
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'jmerazo96'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Jmerazo96*'
app.config['MYSQL_DATABASE_DB'] = 'alpha'

# Intialize MySQL
mysql = MySQL(app)