"""
This module is for defining DB models required for the app.
"""
from datetime import datetime
from src import db


class Product(db.Model):
    """
    A Product DB Model class.

    Author: Sourav Bhatnagar
    Date: 11th May, 2023
    """
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(2000), nullable=True)
    created_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)

    def __repr__(self):
        return f"Product('{self.name}', '{self.created_date}')"


class Location(db.Model):
    """
    A Location DB Model class.

    Author: Sourav Bhatnagar
    Date: 11th May, 2023
    """
    location_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(2000), nullable=True)
    created_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)

    def __repr__(self):
        return f"Location('{self.name}', '{self.created_date}')"


class ProductMovement(db.Model):
    """
    A ProductMovement DB Model class.

    Author: Sourav Bhatnagar
    Date: 11th May, 2023
    """
    movement_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    from_location_id = db.Column(
        db.Integer,
        db.ForeignKey('location.location_id'),
        nullable=True
    )
    to_location_id = db.Column(
        db.Integer,
        db.ForeignKey('location.location_id'),
        nullable=True
    )
    product_id = db.Column(
        db.Integer,
        db.ForeignKey('product.product_id'),
        nullable=False
    )
    qty = db.Column(db.Integer, default=0)
    product = db.relationship(
        "Product", foreign_keys=[product_id])
    from_location = db.relationship(
        "Location", foreign_keys=[from_location_id])
    to_location = db.relationship("Location", foreign_keys=[to_location_id])
    created_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)

    def __repr__(self):
        return f"ProductMovement('{self.timestamp}', '{self.from_location.name}', '{self.to_location.name}', '{self.qty}')"


class Inventory(db.Model):
    """
    A Inventory DB Model class.

    Author: Sourav Bhatnagar
    Date: 11th May, 2023
    """
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(
        db.Integer,
        db.ForeignKey('product.product_id'),
        nullable=False
    )
    location_id = db.Column(
        db.Integer,
        db.ForeignKey('location.location_id'),
        nullable=False
    )
    qty = db.Column(db.Integer, default=0)
    product = db.relationship(
        "Product", foreign_keys=[product_id])
    location = db.relationship(
        "Location", foreign_keys=[location_id])
    created_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    last_modified = db.Column(db.DateTime, nullable=False,
                              default=datetime.utcnow)

    def __repr__(self):
        return f"Inventory('{self.product.name}', '{self.location.name}', '{self.qty}')"
