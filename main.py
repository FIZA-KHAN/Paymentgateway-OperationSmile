from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/"
#app.secret_key = 'super-secret-key'

db = SQLAlchemy(app)

@app.route('/')
def home():
    return(render_template('index.html'))

@app.route('/about')
def about():
    return(render_template('about.html'))

if __name__ == '__main__':
    app.run(debug=True)