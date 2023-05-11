"""
This is a special handler module for error related HTML rendering.
"""

from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    """
    This function render's HTML page for 404 type error.

    :param error: 404 related error object
    :return: Rendered HTML page
    """
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(403)
def error_403(error):
    """
    This function render's HTML page for 403 type error.

    :param error: 403 related error object
    :return: Rendered HTML page
    """
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(500)
def error_500(error):
    """
    This function render's HTML page for 500 type error.

    :param error: 500 related error object
    :return: Rendered HTML page
    """
    return render_template('errors/500.html'), 500
