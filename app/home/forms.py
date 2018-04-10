"""
| Module: forms.py
| Location: app.home
| Purpose: provides the forms for the home route.
"""
from flask_wtf import FlaskForm
from wtforms import (StringField,
                     SubmitField,
                     DateField,
                     IntegerField,
                     SelectField,
                     TextAreaField,
                     HiddenField)

class ProcessTestUsersForm(FlaskForm):
    """Form to enter the number of test users to create."""
    nbr_users = IntegerField('Nbr Test Users')
    submit = SubmitField('Start Creating Testers')
