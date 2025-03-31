from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import mongo
import cv2  # Requiere `pip install opencv-python`
import numpy as np

inspection_bp = Blueprint('inspection', __name__)

@inspection_bp.route('/inspections', methods=['POST'])
@jwt_required()
def add_inspection():
    current_user = get_jwt_identity()
    user = mongo.db.users.find_one({"_id": current_user})
    if user.get("role") not in ["operator", "admin"]:
        return jsonify({"error": "Solo operadores o administradores pueden agregar inspecciones"}), 403
    
    if 'image' not in request.files:
        return jsonify({"error": "Se requiere una imagen"}), 400
    
    file = request.files['image']
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    
    # Procesamiento básico con OpenCV (detección de grietas/baches)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    damage_detected = np.sum(edges) > 10000  # Umbral simple, ajusta según necesidad
    
    inspection_data = {
        "operator_id": current_user,
        "image_path": file.filename,
        "damage_detected": damage_detected,
        "timestamp": request.form.get('timestamp', '')
    }
    mongo.db.inspections.insert_one(inspection_data)
    return jsonify({"message": "Inspección agregada", "damage_detected": damage_detected}), 201

@inspection_bp.route('/inspections', methods=['GET'])
@jwt_required()
def get_inspections():
    inspections = mongo.db.inspections.find()
    return jsonify([{
        "operator_id": str(ins["operator_id"]),
        "image_path": ins["image_path"],
        "damage_detected": ins["damage_detected"],
        "timestamp": ins["timestamp"]
    } for ins in inspections]), 200