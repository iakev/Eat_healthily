#!/usr/bin/env python
"""view to create and get the farmers account"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.farmers import Farmer


@app_views.route('/farmers', methods=['POST'], strict_slashes=False)
def create_farmers():
    """creating a new farmer and saving in the database"""
    if request.get_json() is None:
        abort(400, description="Not a Json request")
    data = request.get_json()
    new_farmer = Farmer(**data)
    new_farmer.save()
    return make_response(jsonify(new_farmer.to_dict(), 201))

@app_views.route('/farmers', methods=['GET'], strict_slashes=True)
def get_farmers():
    """getting all farmers from the database"""
    farmers = []
    all_dict = storage.all(Farmer)
    for obj in all_dict.values():
        farmers.append(obj.to_dict())
    return jsonify(farmers)

@app_views.route('/farmers/<farmer_id>', methods=['GET'], strict_slashes=False)
def get_farmer(farmer_id):
    """get a specific farmer"""
    farmer = storage.get(Farmer, farmer_id)
    if not farmer:
        abort(404)
    return jsonify(farmer.to_dict())

@app_views.route('/farmers/<farmer_id>', methods=['DELETE'], strict_slashes=False)
def delete_farmer(farmer_id):
    """Removes a farmer based on farmer id from database"""
    farmer = storage.get(Farmer, farmer_id)
    if not farmer:
        abort(404, description="Not a valid farmer id")
    farmer.delete()
    return make_response(jsonify({}),200)
    
@app_views.route('/farmers/<farmer_id>', methods=['PUT'], strict_slashes=False)
def update_farmer(farmer_id):
    """Updates a farmer based on the id"""
    if not request.get_json():
        abort(400, desription="Not a valid JSON")
    farmer = storage.get(Farmer, farmer_id)
    if not farmer:
        abort(400, description="Not a valid farmer id")
    ignore = ['created_at', 'id', 'updated_at']
    data = request.get_json()
    for k,v in data.items():
        if k not in ignore:
            setattr(farmer, k, v)
    storage.save()
    return make_response(jsonify(farmer.to_dict()), 200)
