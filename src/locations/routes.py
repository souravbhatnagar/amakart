"""
This module defines the APIs for locations route blueprint.
"""
from flask import (render_template, url_for, flash,
                   redirect, request, Blueprint)
from src import db
from src.models import Location
from src.locations.forms import LocationForm

locations_bp = Blueprint('locations', __name__)


@locations_bp.route("/locations", methods=['GET', 'POST'])
def locations():
    """
    This API function fetches all the added locations from the DB and returns it
    rendered to a HTML doc.

    :return: Rendered HTML page
    """
    if request.method == 'POST':
        form = LocationForm()
        if form.validate_on_submit():
            location = Location(name=form.name.data,
                                description=form.description.data)
            db.session.add(location)
            db.session.commit()
            flash('The location has been added', 'success')
            return redirect(url_for('locations.locations'))
        return render_template('add_location.html',
                               form=form, legend='New Location', method="POST")
    page = request.args.get('page', 1, type=int)
    locations = Location.query.order_by(Location.created_date.desc()).paginate(
        page=page, per_page=12
    )
    return render_template('locations.html', locations=locations)


@locations_bp.route("/locations/<int:location_id>", methods=['GET', 'POST'])
def location(location_id):
    """
    This API function fetchs the location details and returns it rendered
    to a HTML page.

    :param location_id: A unique location Id
    :return: Rendered HTML page
    """
    location = Location.query.get_or_404(location_id)
    if request.form.get('_method') == 'PUT':
        form = LocationForm()
        if form.validate_on_submit():
            location.name = form.name.data
            location.description = form.description.data
            db.session.commit()
            flash('The location details has been updated!', 'success')
            return redirect(url_for('locations.location',
                                    location_id=location.location_id))
        form.name.data = location.name
        form.description.data = location.description
        return render_template('add_location.html', form=form,
                               legend='Update Location', method="PUT")
    if request.form.get('_method') == 'DELETE':
        db.session.delete(location)
        db.session.commit()
        flash('The location has been deleted!', 'success')
        return redirect(url_for('locations.locations'))
    return render_template('location.html', location=location)
