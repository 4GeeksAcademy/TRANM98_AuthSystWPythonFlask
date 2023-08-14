"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/token', methods=['POST'])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or "password" != "test":
        return jsonify({'msg': 'Invalid'}), 401
    
    access_token = create_access_token(identity=email)


    return jsonify(response_body), 200