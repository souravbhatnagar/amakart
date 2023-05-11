"""
This module defines the APIs for main route blueprint.
"""
from flask import render_template, request, Blueprint
from src.models import Inventory

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    """
    This API function returns a rendered home page HTML doc.

    :return: Rendered HTML page
    """
    return render_template('home.html')


@main.route("/about")
def about():
    """
    This API function returns a rendered about page.

    :return: Rendered HTML page
    """
    return render_template('about.html', title='About')


@main.route("/inventory")
def inventory():
    """
    This API function returns a rendered inventory page.

    :return: Rendered HTML page
    """
    page = request.args.get('page', 1, type=int)
    inventory_data = Inventory.query.order_by(Inventory.last_modified.desc()).paginate(
        page=page, per_page=10
    )
    return render_template('inventory.html', inventory_data=inventory_data)
