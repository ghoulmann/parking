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

class Eligibility(FlaskForm):
    #v_make = StringField('Vehicle Make')
    #v_model = StringField('Vehicle Model')
    #v_year = StringField('Vehicle Year')
    full_name = StringField('Full Name', validators=[validators.DataRequired()])
    email = more_fields.EmailField('Email Address', validators=[validators.DataRequired(), validators.Email()])
    registration = BooleanField('Registration')
    consent = BooleanField('Parent/Guardian Written Consent')
    license = BooleanField('Licensed Driver')
    insurance = BooleanField('Insured')
    l_plate = StringField('License Plate', validators=[validators.DataRequired()])
    state = StringField('Registration State')
    grade = SelectField(choices=[(12, '12th'), (11, '11th'), (10,'10th'),  (9,'9th') ])
    submit = SubmitField('Submit')


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
    grade = SelectField(choices=[(12, '12th'), (11, '11th'), (10,'10th'),  (9,'9th') ])

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
