#!/usr/bin/env bash
"""Defining API endpoints for inputs"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.inputs import Input

@app_views.route('/inputs', methods=['GET'], strict_slashes=False)
def get_inputs():
    """Retrieves a list of all inputs"""
    inputs_dict = storage.all(Input)
    inputs = [input.to_dict() for input in inputs_dict.values()]
    return jsonify(inputs)

@app_views.route('/inputs/<input_id>', methods=['GET'], strict_slashes=False)
def get_input(input_id):
    """Retrieve a specific input via it's id"""
    input = storage.get(Input, input_id)
    if not input:
        abort(404)
    return jsonify(input.to_dict())

@app_views.route('/inputs', methods=['POST'], strict_slashes=False)
def post_inputs():
    """Posts a new input"""
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    if 'input_name' not in request.get_json():
        abort(400, description="Missing input_name") 
    if 'source' not in request.get_json():
        abort(400, description="Missing input source")
    data = request.get_json()
    input = Input(**data)
    input.save()
    return make_response(jsonify(input.to_dict(), 201))
    
@app_views.route('/inputs/<input_id>', methods=['PUT'], strict_slashes=False)
def update_input(input_id):
    """Updates a specific input via it's id"""
    if not request.get_json():
        abort(400, description="Not a valid json")
    input = storage.get(Input, input_id)
    if not input:
        abort(404)
    ignore = ['id', 'created_at', 'updated_at']
    data = request.get_json()
    for k,v in data.items():
        if k not in ignore:
            setattr(input, k, v)
    storage.save()
    return make_response(jsonify(input.to_dict()), 200)
    
@app_views.route('/inputs/<input_id>', methods=['DELETE'], strict_slashes=False)
def delete_input(input_id):
    """removes a specific input via it's id"""
    input = storage.get(Input, input_id)
    if not input:
        abort(404)
    input.delete()
    return make_response(jsonify({}), 200)
