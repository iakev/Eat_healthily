#!/usr/bin/env python
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.farms import Farm
from models.products import Produce
from models.operations import Operation

# @app_views.route('/farms/<farm_id>/operations', methods=['GET'], strict_slashes=False)
# def get_farm_operations(farm_id):
#     """Retrieve a list of all operations linked to a specific farm"""
#     farm = storage.get(Farm, farm_id)
#     if not farm:
#         abort(404)
#     operations = [operation.to_dict() for operation in farm.operations]
#     return jsonify(operations)

# @app_views.route('/farms/<farm_id>/products/<product_id>/operations', methods=['GET'], strict_slashes=False)
# def get_product_operations(product_id):
#     """Retrieves a list of all operations linked to a specific product"""
#     produce = storage.get(Produce, product_id)
#     if not produce:
#         abort(404)
#     operations = [operation.to_dict() for operation in produce.operations]
#     return jsonify(operations)
@app_views.route('/operations', methods=['GET'], strict_slashes=False)
def get_operations():
    """Retrieves a list of all operations"""
    operations = [operation.to_dict() for operation in storage.all(Operation).values()]
    return jsonify(operations)

@app_views.route('/operations/<operation_id>', methods=['GET'], strict_slashes=False)
def get_operation(operation_id):
    """Retrieve a specific operation"""
    operation = storage.get(Operation, operation_id)
    if not operation:
        abort(404)
    return jsonify(operation.to_dict())

@app_views.route('/operations', methods=['POST'], strict_slashes=False)
def post_operations():
    """Create an operation"""
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    if 'operation_name' not in request.get_json():
        abort(400, description="Missing operation name")
    data = request.get_json()
    operation = Operation(**data)
    operation.save()
    return make_response(jsonify(operation.to_dict()), 201)

# @app_views.route('farms/<farm_id>/products/<product_id>/operations', methods=['POST'], strict_slashes=False)
# def post_produce_operations(farm_id,product_id):
#     """Creates and links operation to a product linked to a farm"""
#     farm = storage.get(Farm, farm_id)
#     if not farm:
#         abort(404)
#     produce = storage.get(Produce, product_id)
#     if not produce:
#         abort(404)
#     if produce in farm.products:
#         if not request.get_json():
#             abort(400, description="Not a valid JSON")
#         if 'operation_name' not in request.get_json():
#             abort(400, description="Missing operation name")
#         if 'description' not in request.get_json():
#             abort(400, description="Missing description")
#         data = request.get_json()
#         operation = Operation(**data)
#         operation.product_id = produce.id
#         operation.save()
#     else:
#         abort(404)
#     return make_response(jsonify(operation.to_dict()), 201)
    

@app_views.route('/operations/<operation_id>', methods=['PUT'], strict_slashes=False)
def update_operations(operation_id):
    """Updates an operation"""
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    operation = storage.get(Operation, operation_id)
    if not operation:
        abort(404)
    ignore = ['id', 'created_at', 'updated_at']
    data = request.get_json()
    for k,v in data.items():
        if k not in ignore:
            setattr(operation, k, v)
    storage.save()
    return make_response(jsonify(operation.to_dict()), 200)

@app_views.route('/operations/<operation_id>', methods=['DELETE'], strict_slashes=False)
def delete_operation(operation_id):
    """"Deletes a specific operation based on it's id"""
    operation = storage.get(Operation, operation_id)
    if not operation:
        abort(404)
    operation.delete()
    return make_response(jsonify({}), 200)
