"""view to create farms and link to farmers"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.farmers import Farmer
from models.farms import Farm

@app_views.route('/farms', methods=['GET'], strict_slashes=False)
def get_farms():
    """Retrieves a list of all farms"""
    farm_dict = storage.all(Farm)
    farms = [farm.to_dict() for farm in farm_dict.values()]
    return jsonify(farms)

@app_views.route('/farmers/<farmer_id>/farms', methods=['POST'], strict_slashes=False)
@app_views.route('/farmers/<farmer_id>/farms/<farm_id>', methods=['POST'], strict_slashes=False)
def post_farmer_farm(farmer_id, farm_id=None):
    """creates a farm and links it to a farmer or 
        also links an existing farm to an existing farmer"""
    if farm_id:
        farmer = storage.get(Farmer, farmer_id)
        if not farmer:
            abort(404)
        farm = storage.get(Farm, farm_id)
        if not farm:
            abort(404)
        farmer.farms.append(farm)
        storage.save()
    else:
        if request.get_json() is None:
            abort(400, description="Not a JSON request")
        farmer = storage.get(Farmer, farmer_id)
        if not farmer:
            abort(404)
        if 'farm_name' not in request.get_json():
            abort(400, description="Missing farm name")
        if 'address' not in request.get_json():
            abort(400, description="Missing address")
        data = request.get_json()
        data['farmer_id'] = farmer.id
        farm = Farm(**data)
        farm.save()
        if farm in farmer.farms:
            return make_response(jsonify(farm.to_dict(), 201))
        else:
            farmer.farms.append(farm)
            storage.save()
    return make_response(jsonify(farm.to_dict(), 201))

@app_views.route('/farms/<farm_id>/farmers', methods=['GET'], strict_slashes=False)
def get_farmers_farm(farm_id):
    """Retrieves a list of farmers associated with a farm"""
    farm = storage.get(Farm, farm_id)
    if not farm:
        abort(404)
    farmers = [farmer.to_dict() for farmer in farm.farmers]
    return jsonify(farmers)

@app_views.route('/farms/<farm_id>', methods=['GET'], strict_slashes=False)
def get_farm(farm_id):
    """get a specific farm based on farm_id"""
    farm = storage.get(Farm, farm_id)
    if not farm:
        abort(404)
    return jsonify(farm.to_dict())

@app_views.route('/farmers/<farmer_id>/farms', methods=['GET'], strict_slashes=False)
def get_farm_farmers(farmer_id):
    """Retrieve a list of farms asscociated with a particular farmer"""
    farmer = storage.get(Farmer, farmer_id)
    if not farmer:
        abort(404)
    farms = [farm.to_dict() for farm in farmer.farms]
    return jsonify(farms)

@app_views.route('/farms/<farm_id>', methods=['DELETE'], strict_slashes=False)
def get_farmer_farm(farm_id):
    """Deletes a specific farm using it's id"""
    farm = storage.get(Farm, farm_id)
    if not farm:
        abort(404)
    farm.delete()
    return make_response(jsonify({}), 200)

@app_views.route('/farms/<farm_id>', methods=['PUT'], strict_slashes=False)
def put_farm(farm_id):
    """Edit and updates the farm particulars"""
    farm = storage.get(Farm, farm_id)
    if not farm:
        abort(404)
    if not request.get_json():
        abort(400, description="Request Not a JSON")
    ignore = ['id', 'created_at','updated_at']
    data = request.get_json()
    for k,v in data.items():
        if k not in ignore:
            setattr(farm, k, v)
    storage.save()
    return make_response(jsonify(farm.to_dict()), 200)
