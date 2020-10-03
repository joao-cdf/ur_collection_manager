from app import flask_app
from flask import render_template, redirect, request, url_for

#------------------
#oauth
from flask_oauthlib.client import OAuth

oauth = OAuth()

ur_app = oauth.remote_app('urban_rivals',
    base_url = 'https://www.urban-rivals.com/api/',
    request_token_url = 'https://www.urban-rivals.com/api/auth/request_token.php',
    access_token_url = 'http://www.urban-rivals.com/api/auth/access_token.php',
    authorize_url = 'https://www.urban-rivals.com/api/auth/authorize.php',
    consumer_key = '079992a8dbfdc8b6cb4fe8e62695c6ab05f668958',
    consumer_secret = '8e39f1ae339dda74d11ff4e0cef7e535'
)
#---------------------------
#session token saving
from flask import session

@ur_app.tokengetter
def get_ur_token(token=None):
    return session.get('ur_token')
#----------------------------


@flask_app.route('/', methods=['GET','POST'])
@flask_app.route('/index', methods=['GET','POST'])
def index():
    return render_template('index.html', title='Index')

@flask_app.route('/ur_connect', methods=['GET','POST'])
def ur_connect():
    return ur_app.authorize(callback=url_for('ur_authorized'))

@flask_app.route('/ur_authorized', methods=['GET','POST'])
def ur_authorized():
    next_url = request.args.get('next') or url_for('index')
    resp = ur_app.authorized_response()
    if resp is None:
        return redirect(next_url)
    print(resp)

    return redirect(next_url)