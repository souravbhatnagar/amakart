"""
This module is for defining Location related form.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class LocationForm(FlaskForm):
    """
    A Flask form model for Location.

    Author: Sourav Bhatnagar
    Date: 11th May, 2023
    """
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Add')
