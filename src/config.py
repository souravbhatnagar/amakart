"""
This module is for defining Configuration class for the app.
"""
import os


class Config:
    """
    A Configuration class.

    Author: Sourav Bhatnagar
    Date: 11th May, 2023
    """
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
