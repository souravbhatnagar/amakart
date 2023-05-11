"""
This module defines the APIs for products route blueprint.
"""
from flask import (render_template, url_for, flash,
                   redirect, request, Blueprint)
from src import db
from src.models import Product
from src.products.forms import ProductForm

products_bp = Blueprint('products', __name__)


@products_bp.route("/products", methods=['GET', 'POST'])
def products():
    """
    This API function fetches all the added products from the DB and returns it
    rendered to a HTML doc.

    :return: Rendered HTML page
    """
    if request.method == 'POST':
        form = ProductForm()
        if form.validate_on_submit():
            product = Product(
                name=form.name.data,
                description=form.description.data)
            db.session.add(product)
            db.session.commit()
            flash('The product has been added', 'success')
            return redirect(url_for('products.products'))
        return render_template('add_product.html', form=form,
                               legend='New Product', method="POST")
    page = request.args.get('page', 1, type=int)
    products = Product.query.order_by(Product.created_date.desc()).paginate(
        page=page, per_page=12
    )
    return render_template('products.html', products=products)


@products_bp.route("/products/<int:product_id>", methods=['GET', 'POST'])
def product(product_id):
    """
    This API function fetchs the Product details and returns it rendered
    to a HTML page.

    :param product_id: A unique Product Id
    :return: Rendered HTML page
    """
    product = Product.query.get_or_404(product_id)
    if request.form.get('_method') == 'PUT':
        form = ProductForm()
        if form.validate_on_submit():
            product.name = form.name.data
            product.description = form.description.data
            db.session.commit()
            flash('The product details has been updated!', 'success')
            return redirect(url_for('products.product',
                                    product_id=product.product_id))
        form.name.data = product.name
        form.description.data = product.description
        return render_template('add_product.html', form=form,
                               legend='Update Product', method="PUT")
    if request.form.get('_method') == 'DELETE':
        db.session.delete(product)
        db.session.commit()
        flash('The product has been deleted!', 'success')
        return redirect(url_for('products.products'))
    return render_template('product.html', product=product)
