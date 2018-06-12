# -*- coding: utf-8 -*-
import datetime
import json
import os
import time
import csv

from operator import attrgetter


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
from process.process import json_dict_list

#DATABASE = 'sqlite/parking_app.db'

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
csrf = CSRFProtect()
app.config.update(dict(SECRET_KEY = os.urandom(24) or 'riverrun'))

csrf.init_app(app)

Bootstrap(app)
nav = Nav()
app_path = os.path.dirname(os.path.realpath(__file__))
global app_path
global data_path
data_path = app_path + '/data/output.json'
#print data_path

# registers the "top" menubar

nav.register_element('top', Navbar(
    'Parking',
    View('Home', 'home'),
    View('Apply for Permit', 'application'),
    View('Hardship Request', 'hardship_app'),
    Subgroup('Admin',
        View('All Applications', 'view_applications'),
        View('Settings and Configuration', 'settings'),
	View('Create Hardship Permit', 'hardship_admin')
        #Separator(),
        #Label('Discontinued Products'),
        #View('Wg10X', 'products', product='wg10x'),

    ),

))



@app.route('/admin/hardship_app', methods=['GET', 'POST'])
def hardship_admin():
    return render_template('hardship_admin.html')
@app.route('/hardship', methods=['GET', 'POST'])
def hardship_app():

    return render_template('hardship_form.html')


@app.route('/')
def home():
    #cur = get_db().cursor()
    lot = Lot()
    return render_template('index.html', object=lot)
'''
app.route('/eligibility', methods=['GET', 'POST'])
def determine_elig():
    complete = {}
    if request.method == 'POST':

        result = request.form
        for key, value in result.items():
            if key != 'csrf_token':
                if key != 'submit':
                    complete[key] = value
        now = unicode(datetime.datetime.now())
        app_obj = Application('current')
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
'''
@app.route('/application', methods=['GET', 'POST'])
def application():
    complete = {}

    if request.method == 'POST':
        result = request.form.to_dict()
        #complete = result
        for key, value in result.items():
            if key != 'csrf_token':
                if key != 'submit':
                    result[key] = value
        now = unicode(datetime.datetime.now())
        #result['timestamp'] = now

        app_obj = Application(result['full_name'])
        process_form_results(result, app_obj)
        #app_obj.name = complete['full_name']
        #app_obj.licence_plate = complete['l_plate']
        #app_obj.plate_state = complete['state']
        #app_obj.grade = complete['grade']
        app_obj.multiply(app_obj.qualifier)
        app_obj.expo_bloom(app_obj.qualifier, app_obj.raw_score)
        #print application

        '''
        length = len(app_obj.__dict__)
        with open(app_path + '/data/output.csv', 'wb') as test_file:
            csv_writer = csv.writer(test_file, delimiter=',')
            for y in range(length):
                line = flatten(app_obj.__dict__)
                csv_writer.writerow([x for x in line])
        #write_csv((app_path + '/data/output.csv'), app_obj.__dict__)
        '''
        application = json.dumps(app_obj.__dict__)
        with open(data_path, 'a+') as record:
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
    records = json_dict_list(data_path)

    return render_template('applications.html', records=records)
@app.route('/admin/settings')
def settings():
    form = LotConfigForm()
    return render_template('settings.html', form=form, wtf=wtf)
'''
def write_csv(csvfile, fields):
    with open(csvfile, 'a+') as datafile:
        writer = csv.writer(datafile, quoting=csv.QUOTE_ALL)
        row_headers = fields.keys()
        writer.writerow(row_headers)
        for header in row_headers:



            row = [attrgetter(fields[header]) (fields) for header in row_headers]
            for count, column in enumerate(row):

                if callable(column):
                    row[count] = column()
                if type(column) is unicode:
                    row[count] = column.encode('utf-8')

                if type(column) is int:
                    row[count] is column()
                if type(column) is str:
                    row(column) is column()
                if type(column) is float:
                    row(column) is column()

                writer.writerow(row)
'''

'''
def flatten(attributes):

    ret = []
    for i in attributes:
        if isinstance(i, list) or isinstance(i, tuple):
            ret.extend(flatten(i))
        elif isinstance(i, dict):
            ret.extend(flatten(i.items()))
        else:
            ret.append(i)
    print ret
'''


if __name__ == "__main__":

    app.run
