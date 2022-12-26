
from flask import Flask
from flask_cors import CORS

app = Flask(__name__, template_folder='views')

from src.controllers import *
from src.router import *

app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

def run_app():
    app.run(port = 5000, debug=True)