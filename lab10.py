import flask
from flask import render_template
import os 
from flask import send_from_directory  

app=flask.Flask(__name__)

@app.route('/index/')
def index():
    return 'Routed to index()'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<name>/')
def name(name):
    return render_template('name.html', name=name)

@app.route('/css/main.css/')
def cssroute():
    return render_template('css/main.css')

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run()