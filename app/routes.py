from app import flask_app
from flask import render_template

@flask_app.route('/')
@flask_app.route('/index', methods=['GET','POST'])
def index():
    
    return render_template('index.html', title='Index')