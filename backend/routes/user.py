#user.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash
from app import mongo

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['POST'])
@jwt_required()
def add_user():
    current_user = get_jwt_identity()
    user = mongo.db.users.find_one({"_id": current_user})
    if user.get("role") != "admin":
        return jsonify({"error": "Solo administradores pueden agregar usuarios"}), 403
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "El nombre de usuario y la contraseña son requeridos"}), 400

    hashed_password = generate_password_hash(password)  # Hasheamos la contraseña
    mongo.db.users.insert_one({"username": username, "password": hashed_password, "status": "pending"})
    return jsonify({"message": "Usuario agregado como pendiente"}), 201
@user_bp.route('/users/approve/<username>', methods=['PUT'])
@jwt_required()
def approve_user(username):
    current_user = get_jwt_identity()
    user = mongo.db.users.find_one({"_id": current_user})
    if user.get("role") != "admin":
        return jsonify({"error": "Solo administradores pueden aprobar usuarios"}), 403
    
    mongo.db.users.update_one({"username": username}, {"$set": {"status": "approved"}})
    return jsonify({"message": "Usuario aprobado"}), 200

@user_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = mongo.db.users.find({"status": "approved"})
    return jsonify([{"username": user['username'], "role": user.get("role", "operator")} for user in users]), 200