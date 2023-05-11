"""
This module is for defining Product related form.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    """
    A Flask form model for Product.

    Author: Sourav Bhatnagar
    Date: 11th May, 2023
    """
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Add')
