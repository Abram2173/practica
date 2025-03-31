from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from app import mongo

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"message": "Faltan las credenciales"}), 400

        user = mongo.db.users.find_one({"username": username})

        if user and check_password_hash(user['password'], password):
            access_token = create_access_token(identity=user['_id'])
            return jsonify({"access_token": access_token}), 200
        else:
            return jsonify({"message": "Credenciales incorrectas"}), 401

    except Exception as e:
        return jsonify({"message": f"Error interno: {str(e)}"}), 500




#@auth_bp.route('/register', methods=['POST'])
#def register():
#    data = request.get_json()
 #   username = data.get('username', None)
#    password = data.get('password', None)

 #   if not username or not password:
 #       return jsonify({"msg": "El nombre de usuario y la contraseña son requeridos"}), 400

    # Verificar si el usuario ya existe
 #   if mongo.db.users.find_one({"username": username}):
 #      return jsonify({"msg": "El usuario ya existe"}), 400

    # Hashear la contraseña y crear el nuevo usuario
 #   hashed_password = generate_password_hash(password)
  #  mongo.db.users.insert_one({
  #      "username": username,
   #     "password": hashed_password,  # Guardar la contraseña hasheada
  #      "role": "operator"  # Asignar el rol por defecto como "operator"
 #
  #  return jsonify({"msg": "Usuario registrado exitosamente"}), 201
