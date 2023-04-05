#!/usr/bin/env python
"""Module that describes the farmer_produce relationship API endpoints"""
from api.v1.views import app_views
from datetime import datetime
from flask import abort, jsonify, make_response, request
from flask import current_app
from models import storage
from models.farms import Farm, FarmProduce
from models.products import Produce
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}


time_format = "%Y-%m-%d"

def allowed_filename(filename):
    """validate an extension is valid before upload"""
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file(file):
    """Method to upload files and save them in a folder specified"""
    filename = secure_filename(file.filename)
    return filename

@app_views.route('/farms/<farm_id>/products/<product_id>', methods=['POST'], strict_slashes=False)
def post_produce_farm(farm_id, product_id):
    """Links a product with a farm"""
    farm = storage.get(Farm, farm_id)
    if not farm:
        abort(404)
    produce = storage.get(Produce, product_id)
    if not produce:
        abort(404)
    data = request.form.to_dict()
    if request.files:
        if 'image_file' in request.files:
            image_file = request.files['image_file']
            if image_file and allowed_filename(image_file.filename):
                image_file_name = upload_file(image_file)
                image_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'],  image_file_name))
                data['image_file'] = '/uploads' + '/' + image_file_name
    if 'planting_date' not in data:
        abort(400, description="Missing planting_date")
    else:
        date_str = data.get('planting_date')
        planting_date = datetime.strptime(date_str, time_format)
        if not planting_date:
            abort(400, description="Missing planting_date")
    data["planting_date"] = planting_date        
    data["farm_id"] = farm.id
    data["produce_id"] = produce.id
    farm_produce = FarmProduce(**data)
    farm_produce.produce = produce
    farm_produce.save()
    if farm_produce in farm.products:
        return make_response(jsonify(produce.to_dict()), 201)
    else:
        farm.products.append(farm_produce)
    storage.save()
    return make_response(jsonify(produce.to_dict(), 201))

@app_views.route('/farms/<farm_id>/products', methods=['GET'], strict_slashes=False)
def get_farm_products(farm_id):
    """Retrieves a list of products in a farm"""
    farm = storage.get(Farm, farm_id)
    if not farm:
        abort(404)
    products = []
    for farm_produce in farm.products:
        farm_prod_dict = farm_produce.to_dict()
        farm_prod_dict['produce_name'] = farm_produce.produce.produce_name
        products.append(farm_prod_dict)
    return jsonify(products)

@app_views.route('/products/<product_id>', methods=['GET'], strict_slashes=False)
def get_product_farm_products(product_id):
    """Retrieves a list of all farm_producsts asociated with a product"""
    produce = storage.get(Produce, product_id)
    if not produce:
        abort(404)
    farm_products = []
    for farm_produce in produce.farms:
        if farm_produce not in farm_products:
            farm_produce_dict = farm_produce.to_dict()
            farm_produce_dict['produce_name'] = produce.produce_name
            farm_produce_dict['farm_name'] = farm_produce.farm.farm_name
            farm_produce_dict['address'] = farm_produce.farm.address
            farm_products.append(farm_produce_dict)
    return jsonify(farm_products)

@app_views.route('/products/<product_id>/farms', methods=['GET'], strict_slashes=False)
def get_produce_farms(product_id):
    """Retrieves a list of all farms associated with a product"""
    produce = storage.get(Produce, product_id)
    if not produce:
        abort(404)
    farms = []
    for farm_produce in produce.farms:
        if farm_produce.farm.to_dict() not in farms:
            farms.append(farm_produce.farm.to_dict())
    return jsonify(farms)

@app_views.route('/<farm_product_id>', methods=['GET'], strict_slashes=False)
def get_farm_produce(farm_product_id):
    """Retrieves a product info"""
    farm_produce = storage.get(FarmProduce, farm_product_id)
    if not farm_produce:
        abort(404)
    farm_produce_dict = farm_produce.to_dict()
    farm_produce_dict['produce_name'] = farm_produce.produce.produce_name
    return jsonify(farm_produce_dict.to_dict())

@app_views.route("/<farm_product_id>", methods=['PUT'], strict_slashes=False)
def update_farm_produce(farm_product_id):
    """Modifies a product info"""
    farm_produce = storage.get(FarmProduce, farm_product_id)
    if not farm_produce:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a valid json")
    ignore = ['created_at', 'updated_at', 'produce_id', 'farm_id', 'id']
    data = request.get_json()
    for k, v in data.items():
        if k not in ignore:
            if k == "harvest_date" or "planting_date":
                v = datetime.strptime(v, time_format)
            setattr(farm_produce, k, v)
    storage.save()
    farm_produce_dict = farm_produce.to_dict()
    farm_produce_dict['produce_name'] = farm_produce.produce.produce_name
    return jsonify(farm_produce_dict)

@app_views.route('/farms/<farm_id>/products/<product_id>/<farm_product_id>', methods=['DELETE'], strict_slashes=False)
def remove_farm_produce(farm_id, product_id, farm_product_id):
    """Removes a produce from a particular farm"""
    #work on correct cascade to gat this delete working later
    farm = storage.get(Farm, farm_id)
    if not farm:
        abort(404)
    produce = storage.get(Produce, product_id)
    if not produce:
        abort(404)
    farm_produce = storage.get(FarmProduce, farm_product_id)
    if not farm_produce:
        abort(404)
    if farm_produce in farm.products:
        farm.products.remove(farm_produce)
        storage.save()
    else:
        abort(404)
    return make_response(jsonify({}), 200)
