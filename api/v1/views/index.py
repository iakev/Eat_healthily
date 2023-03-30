#!/usr/bin/env python
"""index page showinf the status of REST API"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.consumers import Consumer
from models.farmers import Farmer
from models.farms import Farm
from models.operations import Operation
from models.products import Produce
from models.users import User

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Status of API"""
    return jsonify({"status":"ok"})
