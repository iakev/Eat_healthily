#!/usr/bin/env python
"""view to create and get the farmers account"""
from api.v1.views import app_views
from flask import abort, current_app, jsonify, make_response, request
from models import storage
from models.farmers import Farmer
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


@app_views.route('/farmers', methods=['POST'], strict_slashes=False)
def create_farmers():
    """creating a new farmer and saving in the database"""
    data = request.form.to_dict()
    if request.files:
        if 'image_file' in request.files:
            image_file = request.files['image_file']
            if image_file and allowed_filename(image_file.filename):
                image_file_name = upload_file(image_file)
                image_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'],  image_file_name))
                data['image_file'] = '/uploads' + '/' + image_file_name
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
