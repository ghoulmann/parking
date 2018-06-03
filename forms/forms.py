from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, SelectField
from wtforms import validators
from wtforms.fields import html5 as more_fields
from wtforms.widgets import TextArea
from wtforms.widgets import HiddenInput





class LoginForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ApplicationForm(FlaskForm):


    #identity
    name_first = StringField('First Name', validators=[validators.DataRequired()])

    name_last = StringField('Last Name', validators=[validators.DataRequired()])

    email = more_fields.EmailField('Email Address', validators=[validators.DataRequired(), validators.Email()])

    # Requirements
    license = BooleanField('Licensed Driver')
    insurance = BooleanField('Insured')
    l_plate = StringField('License Plate')
    state = BooleanField('Registration State')
    consent = BooleanField('Parent/Guardian Written Consent')
    grade = SelectField(choices=[(9,'9th'), (10,'10th'), (11, '11th'), (12, '12th')])

    # vehicle
    make = StringField('Vehicle Manufacturer')
    model = StringField('Model')
    year = StringField('Vehicle Year')

    # eligibility
    internship = BooleanField('Internship')
    d_enrollment = BooleanField('Dual Enrollment')

    job = BooleanField('Weekday Work Hours')
    ath_carpool = BooleanField('Team Carpool Host')
    athlete = BooleanField('Seasonal Athlete')
    extracurricular = BooleanField('extracurricular Activities')
    sga = BooleanField('Student Government')
    media_production = BooleanField('Media Production')
    gpa = BooleanField('GPA Advantage')
    attendance = BooleanField('Attendance Advantage')
    narrative = StringField('Explanation', widget=TextArea())
    timestamp = DateTimeField('',widget=HiddenInput())




    submit = SubmitField('Submit')
