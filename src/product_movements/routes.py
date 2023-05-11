"""
This module defines the APIs for product_movements route blueprint.
"""
from flask import (render_template, url_for, flash,
                   redirect, request, Blueprint)
from src import db
from src.product_movements import util
from src.models import ProductMovement, Product, Location, Inventory
from src.product_movements.forms import ProductMovementForm

product_movements_bp = Blueprint('product_movements', __name__)


@product_movements_bp.route("/productMovements", methods=['GET', 'POST'])
def product_movements():
    """
    This API function fetches all the added product movements from the DB and returns it
    rendered to a HTML doc.

    :return: Rendered HTML page
    """
    max_qty = None
    form = ProductMovementForm()
    products = Product.query.order_by(Product.name.asc())
    locations = Location.query.order_by(Location.name.asc())
    if request.method == 'POST':
        product_id = request.form.get("product_id")
        from_location_id = request.form.get("from_location_id")
        to_location_id = request.form.get("to_location_id")
        if from_location_id == to_location_id:
            flash("It seems that you have given same location for both to and from. Please don't act stupid.",
                  'warning')
            return redirect(url_for('product_movements.product_movements'))
        product, from_location, to_location = util.get_product_and_locations_obj(
            product_id, from_location_id, to_location_id)
        if from_location:
            item = Inventory.query.filter_by(location=from_location,
                                             product=product).first()
            if not item:
                flash(
                    f'The product {product.name} is not available at {from_location.name}',
                    'danger')
                return redirect(url_for('product_movements.product_movements'))
            max_qty = item.qty
        if form.validate_on_submit():
            qty = form.qty.data
            util.validate_and_add_product_movement(
                db, product, from_location,
                to_location, qty)
            util.validate_and_update_inventory(
                db, product, from_location,
                to_location, qty
            )
            db.session.commit()
            flash('The product movement has been registered', 'success')
            return redirect(url_for('product_movements.product_movements'))
        return render_template('register_product_movement.html', product_id=product_id,
                               from_location_id=from_location_id, to_location_id=to_location_id,
                               form=form, max_qty=max_qty)
    page = request.args.get('page', 1, type=int)
    product_movements = ProductMovement.query.order_by(
        ProductMovement.timestamp.desc()).paginate(
        page=page, per_page=10
    )
    return render_template('product_movements.html', products=products,
                           locations=locations, product_movements=product_movements)
