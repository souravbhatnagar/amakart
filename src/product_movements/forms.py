"""
This module is for defining ProductMovement related form.
"""
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired


class ProductMovementForm(FlaskForm):
    """
    A Flask form model for ProductMovement.

    Author: Sourav Bhatnagar
    Date: 11th May, 2023
    """
    qty = IntegerField('Quantity', validators=[
                       DataRequired()])
    submit = SubmitField('Move')
