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
    full_name = StringField('Full Name', validators=[validators.DataRequired()])

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
    service = BooleanField('Community Service')
    job = BooleanField('Weekday Work Hours')
    athletics_carpool = BooleanField('Team Carpool Host')
    athletics_captain = BooleanField('Athletic Captian')
    athletics = BooleanField('Seasonal Athlete')
    extracurricular = BooleanField('extracurricular Activities')
    sga = BooleanField('Student Government')
    media_production = BooleanField('Media Production')
    gpa = BooleanField('GPA Advantage')
    distance = BooleanField('Prohibitive Commute')
    weekday_job = BooleanField('weekday_job')
    attendance = BooleanField('Attendance Advantage')
    narrative = StringField('Explanation', widget=TextArea(), validators=[validators.DataRequired()])
    timestamp = DateTimeField('',widget=HiddenInput())




    submit = SubmitField('Submit')
