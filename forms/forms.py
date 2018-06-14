from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField, DateTimeField, SelectField, TextAreaField
from wtforms import validators
from wtforms.fields import html5 as more_fields
from wtforms.widgets import TextArea
from wtforms.widgets import HiddenInput


class LotConfigForm(FlaskForm):
    lot_capacity = IntegerField('Lot Capacity', validators=[validators.DataRequired()], default=75)
    submit = SubmitField('Submit')



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
    full_name = StringField('Full Name', validators=[validators.DataRequired()], render_kw={'class': 'form-control'})
    student_id = StringField('Student ID Number', validators=[validators.DataRequired()], render_kw={'class': 'form-control'})

    email = more_fields.EmailField('School Email Address', validators=[validators.DataRequired(), validators.Email()], render_kw={'class': 'form-control'})

    key = StringField('',widget=HiddenInput())

    # Requirements
    registration = BooleanField('Registration')
    license = BooleanField('Licensed Driver')
    insurance = BooleanField('Insured')
    parent_letter = BooleanField('Parent/Guardian Written Consent')

    l_plate = StringField('License Plate')
    state = StringField('Registration State')
    grade = SelectField(choices=[(12, '12th'), (11, '11th'), (10,'10th'),  (9,'9th') ], render_kw={'class': 'form-control'})

    # vehicle
    make = StringField('Vehicle Manufacturer', render_kw={'class': 'form-control'})
    model = StringField('Model', render_kw={'class': 'form-control'})
    year = StringField('Vehicle Year', render_kw={'class': 'form-control'})

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
    attendance = BooleanField('Attendance Advantage')
    narrative = TextAreaField('Please provide details to support your request for a parking permit', validators=[validators.DataRequired(), validators.length(max=750)], render_kw={'class': 'form-control', 'rows': 15})





    submit = SubmitField('Submit')
