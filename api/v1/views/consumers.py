#!/usr/bin/env python
"""view to create and get the consumers account"""
from api.v1.views import app_views
from flask import abort, current_app, jsonify, make_response, request
from models.consumers import Consumer
from models import storage
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

@app_views.route('/consumers', methods=['POST'], strict_slashes=False)
def create_consumers():
    """creating a new consumer and saving in the database"""
    data = request.form.to_dict()
    if request.files:
        if 'image_file' in request.files:
            image_file = request.files['image_file']
            if image_file and allowed_filename(image_file.filename):
                image_file_name = upload_file(image_file)
                image_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'],  image_file_name))
                data['image_file'] = '/uploads' + '/' + image_file_name
    new_consumer = Consumer(**data)
    new_consumer.save()
    return make_response(jsonify(new_consumer.to_dict(), 201))

@app_views.route('/consumers', methods=['GET'], strict_slashes=True)
def get_users():
    """getting consumers from the database"""
    consumers = []
    all_dict = storage.all("Consumer") #modify here to get only the consumers
    for obj in all_dict.values():
        consumers.append(obj.to_dict())
    return jsonify(consumers)
