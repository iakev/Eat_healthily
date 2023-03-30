#!/usr/bin/env python
"""view to create and get the consumers account"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models.consumers import Consumer
from models import storage


@app_views.route('/consumers', methods=['POST'], strict_slashes=False)
def create_consumers():
    """creating a new consumer and saving in the database"""
    if request.get_json() is None:
        abort(400, description="Not a Json request")
    data = request.get_json()
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
