from flask import Flask,render_template,request,redirect,url_for,abort,session
from flask_assets import Environment
from webassets.loaders import PythonLoader as PythonAssetsLoader
import os

import assets

app = Flask(__name__)

assets_env = Environment(app)
assets_loader = PythonAssetsLoader(assets)
for name,bundle in assets_loader.load_bundles().iteritems():
    assets_env.register(name,bundle)

env = os.environ.get('EXAMPLE_ENV','prod')#will default to production env if no var exported
app.config.from_object('example.settings.%sConfig' %env.capitalize())
app.config['ENV'] = env

from models import *
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'asldkjaslduredj'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://example.db'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup',methods=['POST'])
def signup():
    user = User(request.form['username'], request.form['message'])
    db.session.add(user)
    db.session.commit()
    #session['username'] = request.form['username']
    #session['message'] = request.form['message']
    #return redirect(url_for('message'))
    return redirect(url_for('message'),username = user.username)

@app.route('/message<username>')
def message(username):
    #if not 'username' in session:
    #    return abort(403)
    user = User.query.filter_by(username=username).first_or_404()
    #return render_template('message.html',username = session['username'],message = session['message'])
    return render_template('message.html',username = user.username,message = user.message)

if __name__ == '__main__':
    app.run()
