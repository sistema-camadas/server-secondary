from views.response_view import success, created, not_found, bad_request, deleted
from flask import Blueprint, request, jsonify
from models.user_model import User
from models.database import db

user_bp = Blueprint('user_bp', __name__)

## Buscar todos os usuários ##
@user_bp.route('/users', methods=['GET']) 
def get_all_users():
    users = User.query.all()
    return success(data=[user.to_dict() for user in users])

## Buscar usuário por ID ##
@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return not_found()
    return success(data=user.to_dict())

