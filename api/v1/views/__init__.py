#!/usr/bin/env python
"""Blueprint for the api views"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
 
from api.v1.views.consumers import *
from api.v1.views.farm_operations import *
from api.v1.views.farmers import *
from api.v1.views.farmers_farms import *
from api.v1.views.farms_products import *
from api.v1.views.index import *
from api.v1.views.inputs import *
from api.v1.views.operation_inputs import *
from api.v1.views.operations import *
from api.v1.views.operations_products import *
from api.v1.views.products import *
from api.v1.views.users import *