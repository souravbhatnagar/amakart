"""
This is a special utility module for product_movements APIs.
"""
from datetime import datetime
from src.models import ProductMovement, Product, Location, Inventory


def get_product_and_locations_obj(product_id, from_location_id,
                                  to_location_id):
    """
    This function creates Product and Location objects for
    the specified product and location Ids.

    :param product_id: A unique Product Id
    :param from_location_id: A unique Location Id of source
    :param to_location_id: A unique Location Id of destination
    :return: Product and Location objects
    """
    product = Product.query.get(int(product_id))
    from_location = None
    to_location = None
    if from_location_id:
        from_location = Location.query.get(int(from_location_id))
    if to_location_id:
        to_location = Location.query.get(int(to_location_id))
    return product, from_location, to_location


def validate_and_add_product_movement(db, product, from_location,
                                      to_location, qty):
    """
    This function creates a ProductMovement data entry into the DB.

    :param db: A DB session object
    :param product: A DB object of the product
    :param from_location: A DB object of the source Location
    :param to_location: A DB object of the destination Location
    :param qty: The quantity of the product
    :return: None
    """
    product_movement = ProductMovement(
        timestamp=datetime.utcnow(),
        from_location=from_location,
        to_location=to_location,
        product=product,
        qty=qty
    )
    db.session.add(product_movement)


def validate_and_update_inventory(db, product, from_location,
                                  to_location, qty):
    """
    This function updates or creates an Inventory data entry into the DB.

    :param db: A DB session object
    :param product: A DB object of the product
    :param from_location: A DB object of the source Location
    :param to_location: A DB object of the destination Location
    :param qty: The quantity of the product
    :return: None
    """
    if from_location:
        inventory = Inventory.query.filter_by(
            location=from_location, product=product).first()
        inventory.qty = inventory.qty - qty
        inventory.last_modified = datetime.utcnow()
    if to_location:
        inventory = Inventory.query.filter_by(
            location=to_location, product=product).first()
        if not inventory:
            inventory = Inventory(
                product=product,
                location=to_location,
                qty=qty
            )
            db.session.add(inventory)
        else:
            inventory.qty = inventory.qty + qty
            inventory.last_modified = datetime.utcnow()
