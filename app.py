# -*- coding: utf-8 -*-
import datetime
import json
import os
import time


import wtforms as wtf
from flask import Flask, jsonify, redirect, render_template, request, url_for
#from flask_nav import *
#from flask_nav.elements import *
from flask_bootstrap import Bootstrap
#from flask import url_for, render_template
#from flask_bootstrap import Bootstrap
#from flask_nav.elements import *
from flask_nav import Nav
from flask_nav.elements import Link, Navbar, Separator, Subgroup, Text, View
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from forms.forms import ApplicationForm
from wtforms import *
from wtforms.validators import DataRequired
from lot.lot import Lot
from application.application import Application
import sqlite3
from flask import g
from application.application import process_form_results

#DATABASE = 'sqlite/parking_app.db'
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

    '''
    def get_db():
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(DATABASE)
        return db

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()
    '''

    # registers the "top" menubar

    nav.register_element('top', Navbar(
        'Parking',
        View('Home', 'home'),
        View('Application', 'application'),
        Subgroup('Admin',
            View('All Applications', 'view_applications'),
            View('Settings and Configuration', 'settings'),
            #Separator(),
            #Label('Discontinued Products'),
            #View('Wg10X', 'products', product='wg10x'),

        ),

    ))





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
        #cur = get_db().cursor()
        lot = Lot()
        return render_template('index.html', object=lot)

    @app.route('/application', methods=['GET', 'POST'])
    def application():
        complete = {}
        if request.method == 'POST':
            result = request.form

            for key, value in result.items():
                if key != 'csrf_token':
                    if key != 'submit':
                        complete[key] = value
            now = unicode(datetime.datetime.now())
            complete['timestamp'] = now

            #print application



            app_obj = Application(complete['full_name'])
            process_form_results(complete, app_obj)
            app_obj.id = complete['full_name']
            app_obj.grade = complete['grade']
            app_obj.multiply(app_obj.qualifier)
            app_obj.expo_bloom(app_obj.qualifier, app_obj.raw_score)
                        #print application

            application = json.dumps(app_obj.__dict__)
            with open("data/output.json", "a") as record:
                record.write(application + '\n\n')

            return render_template('ack.html', result=complete, object=app_obj)
        else:
            form = ApplicationForm()
            return render_template('application_form.html', title="Application", form=form, wtf=wtf)

    @app.route('/receipt')
    def acknowledge():
        return render_template('ack.html')

    nav.init_app(app)

    @app.route('/admin/applications')
    def view_applications():
        with open('data/output.json') as data:
            records = data.read()
            records = records.split('\n\n')
            for record in records:
                record = record.strip()
                record = json.loads(record)
                try:
                    if record['email']:
                        record = record
                except:
                    pass
        return render_template('applications.html', records=records)
    @app.route('/admin/settings')
    def settings():
        return render_template('settings.html')
    return app



if __name__ == "__main__":

    create_app()
