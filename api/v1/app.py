#!/usr/bin/env python
"""Module that configiures and runs the api"""
from models import storage
from api.v1.views import app_views
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from


UPLOAD_FOLDER = '/home/kirimi/alx/portfolio_project/Eat_healthily/web_app/public/uploads'


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*":{"origins":"*"}})

@app.teardown_appcontext
def close_db(error):
    """close storage"""
    storage.close()

@app.errorhandler(404)
def page_not_found(error):
    """custom page for error"""
    return make_response(jsonify({'error':'Not found'}), 404)

#configure swagger for this
Swagger(app)

if __name__ == "__main__":
    """get the api up and running"""
    host = '0.0.0.0'
    port = '5000'
    app.run(host=host, port=port, threaded=True)
