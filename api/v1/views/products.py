#!/usr/bin/env python
"""Module that describes the produce API endpoints"""
from api.v1.views import app_views
from flask import current_app
from flask import abort, jsonify, make_response, request
from models import storage
from models.products import Produce


@app_views.route('/products', methods=['GET'], strict_slashes=False)
def get_products():
    """Retrieves a list of all products in the database"""
    products_dict = storage.all(Produce)
    products = [product.to_dict() for product in products_dict.values()]
    return jsonify(products)

@app_views.route('/products/<produce_id>', methods=['GET'], strict_slashes=False)
def get_product(produce_id):
    """Retrieves a single products in the database"""
    produce = storage.get(Produce, produce_id)
    if not produce:
        abort(404)
    return jsonify(produce.to_dict())

@app_views.route('/products' ,methods=['POST'], strict_slashes=False)
def post_product():
    """Creates a product and adds to the database"""
    if request.get_json() is None:
        abort(400, description="Not a valid JSON")
    if 'produce_name' not in request.get_json():
        abort(400, description="Missing produce name")
    data = request.get_json()
    produce = Produce(**data)
    produce.save()
    return make_response(jsonify(produce.to_dict()), 201)

@app_views.route('/products/<produce_id>', methods=['PUT'], strict_slashes=False)
def update_product(produce_id):
    """Updates a single products in the database"""
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    produce = storage.get(Produce, produce_id)
    if not produce:
        abort(404)
    ignore = ['id', 'created_at', 'updated_at']
    data = request.get_json()
    for k,v in data.items():
        if k not in ignore:
            setattr(produce, k, v)
    storage.save()
    return jsonify(produce.to_dict())

@app_views.route('/products/<produce_id>', methods=['DELETE'], strict_slashes=False)
def delete_product(produce_id):
    """Deletes a single products in the database"""
    produce = storage.get(Produce, produce_id)
    if not produce:
        abort(404)
    produce.delete()
    return make_response(jsonify({}), 200)
