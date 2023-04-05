#!/usr/bin/env bash
"""Defining API endpoints for inputs"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flask import current_app
from models import storage
from models.inputs import Input
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}

def allowed_filename(filename):
    """validate an extension is valid before upload"""
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file(file):
    """Method to upload files and save them in a folder specified"""
    filename = secure_filename(file.filename)
    return filename

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
    tox_level_dic = {"1" : "Highly toxic", "2" :"Toxic", 
                     "3": "Moderately toxic", 
                     "4" :"Slightly toxic","5": "Virtually non-toxic"}
    data = request.form.to_dict()
    if 'input_name' not in data:
        abort(400, description="Missing input_name") 
    if 'source' not in data:
        abort(400, description="Missing input source")
    if request.files:
        if 'image_file' in request.files:
            image_file = request.files['image_file']
            if image_file and allowed_filename(image_file.filename):
                image_file_name = upload_file(image_file)
                image_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'],  image_file_name))
                data['image_file'] = '/uploads' + '/' + image_file_name
        if 'label_file' in request.files:
            label_file = request.files['label_file']
            if label_file and allowed_filename(label_file.filename):
                label_file_name = upload_file(label_file)
                label_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'],  label_file_name))
                data['label_file'] = '/uploads' + '/' + label_file_name
        if 'user_manual_file' in request.files:
            user_manual_file = request.files['user_manual_file']
            if user_manual_file and allowed_filename(user_manual_file.filename):
                user_manual_file_name = upload_file(user_manual_file)
                user_manual_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'],  user_manual_file_name))
                data['user_manual_file_name'] = '/uploads' + '/' + user_manual_file_name
    if data['toxicity_level'] in tox_level_dic.keys():
        data['toxicity_level'] = tox_level_dic[data['toxicity_level']] 
    input = Input(**data)
    inputs = [value for value in storage.all(Input).values()]
    for current_input in inputs:
        if current_input.input_name == input.input_name:
            return jsonify(current_input.to_dict())
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
