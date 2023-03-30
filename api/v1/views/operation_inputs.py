#!/usr/bin/env python
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.farms import FarmProduce, FarmProduceOperation
from models.operations import Operation
from models.inputs import Input

@app_views.route('/farm_produce/<farm_produce_id>/<farm_produce_operation_id>/inputs/<input_id>', methods=['POST'], strict_slashes=False)
def post_operation_input(farm_produce_id,farm_produce_operation_id,input_id):
    """Links an input to an operation"""
    farm_produce = storage.get(FarmProduce, farm_produce_id)
    if not farm_produce:
        abort(404)
    farm_produce_operation = storage.get(FarmProduceOperation, farm_produce_operation_id)
    if not farm_produce_operation:
        abort(404)
    input = storage.get(Input, input_id)
    if not input:
        abort(404)
    if input not in farm_produce_operation.inputs:
        farm_produce_operation.inputs.append(input)
    else:
        return make_response(jsonify(input.to_dict()), 201)
    storage.save()
    return make_response(jsonify(input.to_dict()), 201)

@app_views.route('/farm_produce_operations/<farm_produce_operation_id>/inputs', methods=['GET'], strict_slashes=False)
def get_operation_inputs(farm_produce_operation_id):
    """Retrieves a list of all inputs associated with an operation"""
    farm_produce_operation = storage.get(FarmProduceOperation, farm_produce_operation_id)
    if not farm_produce_operation:
        abort(404)
    inputs = [input.to_dict() for input in farm_produce_operation.inputs]
    return jsonify(inputs)


@app_views.route('/inputs/<input_id>/operations', methods=['GET'], strict_slashes=False)
def get_input_operations(input_id):
    """Retrieves a list of all operations associated with an input"""
    input = storage.get(Input, input_id)
    if not input:
        abort(404)
    operations = [operation.to_dict() for operation in input.operations]
    return jsonify(operations)

@app_views.route('/operations/<operation_id>/inputs/<input_id>', methods=['DELETE'], strict_slashes=False)
def delete_operation_input(operation_id, input_id):
    """Unlinks an input from an operation"""
    operation = storage.get(Operation, operation_id)
    if not operation:
        abort(404)
    input = storage.get(Input,input_id)
    if not input:
        abort(404)
    if input in operation.inputs:
        operation.inputs.remove(input)
    else:
        abort(404)
    return make_response(jsonify({}), 200)
