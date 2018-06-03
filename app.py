# -*- coding: utf-8 -*-
import os

from flask import Flask
#from flask import url_for, render_template
#from flask_bootstrap import Bootstrap
#from flask_nav.elements import *
from flask_nav import Nav
from flask import Flask, render_template, url_for
#from flask_nav import *
#from flask_nav.elements import *
from flask_bootstrap import Bootstrap
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
from forms.forms import ApplicationForm
from flask_wtf.csrf import CSRFProtect
import wtforms as wtf



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    csrf = CSRFProtect()
    app.config.update(dict(SECRET_KEY = os.urandom(24) or 'riverrun'))

    csrf.init_app(app)

    '''
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    '''
    Bootstrap(app)
    nav = Nav()





    # registers the "top" menubar
    '''
    nav.register_element('top', Navbar(
        View('Start', 'home')
        #View('Our Mission', 'about'),
        Subgroup(
            'Products',
            View('Wg240-Series', 'products', product='wg240'),
            View('Wg250-Series', 'products', product='wg250'),
            Separator(),
            Label('Discontinued Products'),
            View('Wg10X', 'products', product='wg10x'),
        ),

    ))
    '''

    '''
    @nav.navigation()
    def mynavbar():

        return Navbar(
            'Parking',
        View('Home', '/'),
        #View('Request', 'request')
    )
    '''

    '''
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    '''

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/application')
    def application():
        form = ApplicationForm()

        return render_template('application_form.html', title="Application", form=form, wtf=wtf)

    #nav.init_app(app)

    return app
if __name__ == "__main__":

    app.run
