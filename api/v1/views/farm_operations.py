#!/usr/bin/env python
from api.v1.views import app_views
from datetime import datetime
from flask import abort, jsonify, make_response, request
from models import storage
from models.farms import Farm, FarmOperation
from models.operations import Operation

time_format = "%d-%m-%YT%H:%M"
@app_views.route('/farms/<farm_id>/operations/<operation_id>', methods=['POST'], strict_slashes=False)
def post_farm_operation(farm_id, operation_id):
    """Link an operation to a farm"""
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    farm = storage.get(Farm, farm_id)
    if not farm:
        abort(404)
    operation = storage.get(Operation, operation_id)
    if not operation:
        abort(404)
    if not 'operation_date' in request.get_json():
        abort(400, description="Missing operation_date")
    else:
        data  = request.get_json()
        operation_date_str = data.get('operation_date')
        operation_date = datetime.strptime(operation_date_str, time_format)
        if not operation_date:
            abort(400, description="Missing operation_date")
    if not 'description' in request.get_json():
        abort(400, description="Missing description")
    data['operation_date'] = operation_date
    data['farm_id'] = farm.id
    data['operation_id'] = operation.id
    farm_operation = FarmOperation(**data)
    farm_operation.operation = operation
    farm_operation.save()
    if farm_operation in farm.operations:
        return make_response(jsonify(farm_operation.to_dict()), 201)
    else:
        farm.operations.append(farm_operation)
    storage.save()
    return make_response(jsonify(farm_operation.to_dict()), 201)

@app_views.route('/farms/<farm_id>/operations', methods=['GET'], strict_slashes=False)
def get_farm_operations(farm_id):
    """Retrieve a list of all operations associated with a particular farm"""
    farm = storage.get(Farm, farm_id)
    if not farm:
        abort(404)
    operations = []
    for farm_operation in farm.operations:
        farm_operation_dict = farm_operation.to_dict()
        farm_operation_dict['operation_name'] = farm_operation.operation.operation_name
        operations.append(farm_operation_dict)
    return jsonify(operations)

@app_views.route('/operations/<operation_id>/farms', methods=['GET'], strict_slashes=False)
def get_operation_farms(operation_id):
    """Retrieves a list of all farms associated with an operation"""
    operation = storage.get(Operation, operation_id)
    if not operation:
        abort(404)
    farms = []
    for farm_operation in operation.farms:
        if farm_operation.farm.to_dict() not in farms:
            farms.append(farm_operation.farm.to_dict())
    return jsonify(farms)

@app_views.route('/<farm_operation_id>', methods=['GET'], strict_slashes=False)
def get_farm_operation(farm_operation_id):
    """Get a specific farm_operation"""
    farm_operation = storage.get(FarmOperation, farm_operation_id)
    if not farm_operation:
        abort(404)
    farm_operation_dict = farm_operation.to_dict()
    farm_operation_dict['operation_name'] = farm_operation.operation.operation_name
    return jsonify(farm_operation_dict)

@app_views.route('/<farm_operation_id>', methods=['PUT'], strict_slashes=False)
def update_farm_operation(farm_operation_id):
    """Updates a farm_operation"""
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    farm_operation = storage.get(FarmOperation, farm_operation_id)
    if not farm_operation:
        abort(404)
    ignore = ['id', 'created_at', 'updated_at', 'farm_id', 'operation_id']
    data = request.get_json()
    for k, v in data.items():
        if k not in ignore:
            if k == "operation_date":
                v = datetime.strptime(v, time_format)
            setattr(farm_operation, k, v)
    storage.save()
    farm_operation_dict = farm_operation.to_dict()
    farm_operation_dict['operation_name'] = farm_operation.operation.operation_date
    return(jsonify(farm_operation_dict))


@app_views.route('/farms/<farm_id>/operations/<operation_id>', methods=['DELETE'], strict_slashes=False)
def delete_farm_operation(farm_id, operation_id):
    """Unlink an operation from a specific farm"""
    #work on setting the correct cascade to effectively delete relationships
    farm = storage.get(Farm, farm_id)
    if not farm:
        abort(404)
    operation = storage.get(Operation, operation_id)
    if not operation:
        abort(404)
    if operation in farm.operations:
        farm.operations.remove(operation)
    else:
        abort(404)
    return make_response(jsonify({}), 200)
