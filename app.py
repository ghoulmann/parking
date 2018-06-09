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
from forms.forms import ApplicationForm, Eligibility
from wtforms import *
from wtforms.validators import DataRequired
from lot.lot import Lot
from application.application import Application
import sqlite3
from flask import g
from application.application import process_form_results

#DATABASE = 'sqlite/parking_app.db'

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
csrf = CSRFProtect()
app.config.update(dict(SECRET_KEY = os.urandom(24) or 'riverrun'))

csrf.init_app(app)

Bootstrap(app)
nav = Nav()


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







@app.route('/')
def home():
    #cur = get_db().cursor()
    lot = Lot()
    return render_template('index.html', object=lot)
@app.route('/eligibility', methods=['GET', 'POST'])
def determine_elig():
    complete = {}
    if request.method == 'POST':

        result = request.form
        for key, value in result.items():
            if key != 'csrf_token':
                if key != 'submit':
                    complete[key] = value
        now = unicode(datetime.datetime.now())
        app_obj = Application(complete['full_name'])
        process_form_results(complete, app_obj)

        complete['timestamp'] = now

        app_obj.full_name = complete['full_name']
        app_obj.email = complete['email']
        app_obj.grade = complete['grade']
        app_obj.insured = complete['insurance']
        app_obj.license = complete['license']
        app_obj.registration = complete['registration']
        app_obj.consent = complete['consent']
        app_obj.l_plate = complete['l_plate']
        #if (app_obj.grade == 12 and app_obj.insured and app_obj.registration and app_obj.license and app_obj.consent and app_obj.email and app_obj.l_plate):
        if app_obj.grade == 12:
            #return render_template('application.html', result=complete, object=app_obj)
            form = ApplicationForm()
            return render_template('application_form.html', title="Application", result=complete, object=app_obj, form=form, wtf=wtf)
        else:
            return render_template('deny_eligibility.html', object=app_obj)

    else:
        form = Eligibility()
        return render_template('eligibility.html', title="Determine Eligibility", form=form, wtf=wtf)
@app.route('/deny', methods=['GET'])
def deny_eligibility():
    return render_template('deny_eligibility.html', title="Eligibility Determined")
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
        with open("/home/ghoulmann/parking_app/data/output.json", 'a+') as record:
            prior = record.read()
            if prior:
                record.write('\n\n' + application)
            else:
                record.write(application)

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
    with open('/home/ghoulmann/parking_app/data/output.json') as data:
        records = data.read()
        records = records.split('\n\n')
        for record in records:
            record = record.strip()
            record = json.loads(record)

    return render_template('applications.html', records=records)
@app.route('/admin/settings')
def settings():
    return render_template('settings.html')




if __name__ == "__main__":

    app.run
