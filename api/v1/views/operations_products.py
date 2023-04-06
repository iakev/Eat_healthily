#!/usr/bin/env python
"""Defines the relationship betwen operations and products API endpoints"""
from api.v1.views import app_views
from datetime import datetime, timedelta
from flask import abort, jsonify, make_response, request
from models import storage
from models.farms import Farm, FarmProduce, FarmProduceOperation
from models.inputs import Input
from models.operations import Operation
from models.products import Produce

time_format = "%Y-%m-%d" # note to ensure this format in front-end forms
@app_views.route('/farms/<farm_id>/products/<product_id>/<farm_product_id>/operations/<operation_id>', methods=['POST'], strict_slashes=False)
@app_views.route('/farms/<farm_id>/products/<product_id>/<farm_product_id>/operations/<operation_id>/inputs/<input_id>', methods=['POST'], strict_slashes=False)
def post_product_operation(farm_id,product_id,farm_product_id, operation_id, input_id=None):
    """Links an operatioin to a product, add description and operation date during linking"""
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    farm = storage.get(Farm, farm_id)
    if not farm:
        abort(404)
    product = storage.get(Produce, product_id)
    if not product:
        abort(404)
    farm_produce = storage.get(FarmProduce, farm_product_id)
    if not farm_produce:
        abort(404)
    operation = storage.get(Operation, operation_id)
    if not operation:
        abort(404)
    if 'operation_date' not in request.get_json():
        abort(400, description="Missing operation_date")
    else:
        data = request.get_json()
        operation_date_str = data.get('operation_date')
        operation_date = datetime.strptime(operation_date_str, time_format)
    if not operation_date:
        abort(400, description="Missing operation_date")
    description = data.get('description')
    if not description:
        abort(400, description="Missing description")
    if operation.operation_name == "Harvesting" or operation.operation_name == "harvesting":
        farm_produce.harvest_date =  operation_date       
    data['farm_produce_id'] = farm_produce.id    
    data['operation_id'] = operation.id
    data['operation_date'] = operation_date
    farm_produce_operation = FarmProduceOperation(**data)
    farm_produce_operation.operation = operation
    if input_id:
        input = storage.get(Input, input_id)
        if input:
            if input not in farm_produce_operation.inputs:
                farm_produce_operation.inputs.append(input)
    farm_produce_operation.save()
    if farm_produce_operation in farm_produce.operations:
        return make_response(jsonify(operation.to_dict()), 201)
    else:
        farm_produce.operations.append(farm_produce_operation)
    storage.save()
    return make_response(jsonify(operation.to_dict()), 201)


@app_views.route('/farm_products/<farm_product_id>/operations', methods=['GET'], strict_slashes=False)
def get_product_operations(farm_product_id):
    """Retrieves a list of operations done to a particular product"""
    farm_produce= storage.get(FarmProduce, farm_product_id)
    if not farm_produce:
        abort(404)
    operations = []
    for farm_produce_operation in farm_produce.operations:
        farm_produce_operation_dict = farm_produce_operation.to_dict()
        farm_produce_operation_dict['produce_name'] = farm_produce.produce.produce_name
        farm_produce_operation_dict['planting_date'] = farm_produce.planting_date
        farm_produce_operation_dict['harvest_date'] = farm_produce.harvest_date
        farm_produce_operation_dict['farm-name'] = farm_produce.farm.farm_name
        farm_produce_operation_dict['address'] = farm_produce.farm.address
        farm_produce_operation_dict['operation_name'] = farm_produce_operation.operation.operation_name
        farm_produce_operation_dict['inputs'] = []
        for input in farm_produce_operation.inputs:
            farm_produce_operation_dict['inputs'].append(input.to_dict())
            if input.pre_harvest_interval and timedelta(int(input.pre_harvest_interval)) < (farm_produce_operation_dict['harvest_date'] - farm_produce_operation.operation_date):
                farm_produce_operation_dict['phi_safe'] = True
            else:
                farm_produce_operation_dict['phi_safe'] = False
            if input.toxicity_level and (input.toxicity_level !='Slightly toxic' or input.toxicity_level != 'Virtually non-toxic'):
                farm_produce_operation_dict['toxic_safe'] = False
            else:
                farm_produce_operation_dict['toxic_safe'] = True
            if input.expiry_date and input.expiry_date < farm_produce_operation.operation_date:
                farm_produce_operation_dict['expiry_safe'] = False
            else:
                farm_produce_operation_dict['expiry_safe'] = True
        if len(farm_produce_operation.inputs) == 0:
            farm_produce_operation_dict['phi_safe'] = True
            farm_produce_operation_dict['toxic_safe'] = True
            farm_produce_operation_dict['expiry_safe'] = True
        if farm_produce_operation_dict not in operations:
            operations.append(farm_produce_operation_dict)
    return jsonify(operations)

@app_views.route('/operations/<operation_id>/products', methods=['GET'], strict_slashes=False)
def get_operation_products(operation_id):
    """Retrieve a list of all products associated with one operation"""
    operation = storage.get(Operation, operation_id)
    if not operation:
        abort(404)
    products = []
    for produce_operations in operation.products:
        if produce_operations.produce.to_dict() not in products:
            products.append(produce_operations.produce.to_dict())
    return jsonify(products)


@app_views.route('/<farm_produce_operation_id>', methods=['PUT'], strict_slashes=False)
def get_produce_operation(farm_produce_operation_id):
    """Update a specific operation"""
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    farm_produce_operation = storage.get(FarmProduceOperation, farm_produce_operation_id)
    if not farm_produce_operation:
        abort(404)
    ignore = ['id', 'created_at', 'updated_at', 'product_id', 'operation_id']
    data = request.get_json()
    for k, v in data.items():
        if k not in ignore:
            if k == "operation_date":
                v = datetime.strptime(v, time_format)
            setattr(farm_produce_operation, k, v)
    storage.save()
    farm_produce_operation_dict = farm_produce_operation.to_dict()
    farm_produce_operation_dict['operation_name'] = farm_produce_operation.operation.operation_name
    return jsonify(farm_produce_operation_dict)

@app_views.route('/products/<product_id>/operations/<operation_id>', methods=['DELETE'], strict_slashes=True)
def delete_product_operation(product_id, operation_id):
    """Removes an operation from a product"""
    produce = storage.get(Produce, product_id)
    if not produce:
        abort(404)
    operation = storage.get(Operation, operation_id)
    if not operation_id:
        abort(404)
    if operation in produce.operations:
        produce.operations.remove(operation)
    else:
        abort(404)
    return make_response(jsonify({}), 200)
