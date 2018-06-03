from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import validators
from wtforms.fields import html5 as more_fields





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

    # vehicle
    make = StringField('Vehicle Manufacturer')
    model = StringField('Model')
    year = StringField('Vehicle Year')

    # eligibility
    internship = BooleanField('Internship')
    job = BooleanField('Weekday Work Hours')
    ath_carpool = BooleanField('Team Carpool Host')
    athlete = BooleanField('Seasonal Athlete')
    extracurricular = BooleanField('extracurricular Activities')
    sga = BooleanField('Student Government')
    media_production = BooleanField('Media Production')
    gpa = BooleanField('GPA Advantage')
    attendance = BooleanField('Attendance Advantage')




    submit = SubmitField('Submit')
