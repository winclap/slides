from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hola PyConAr 2017 Córdoba!!'
