from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
import os
import logging
from werkzeug.security import generate_password_hash


# Cargar el archivo .env
load_dotenv()

# Inicializar objetos
mongo = PyMongo()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)

    # Permitir solicitudes desde http://localhost:5173 y http://127.0.0.1:5173
    CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://127.0.0.1:5173"]}})

    # Configuración de MongoDB y JWT
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    app.config["FLASK_ENV"] = os.getenv("FLASK_ENV", "development")

    # Log de inicialización
    logger.info("Inicializando MongoDB...")
    mongo.init_app(app)
    logger.info("MongoDB inicializado")

    JWTManager(app)

    # Crear un usuario administrador con contraseña hasheada si no existe
    hashed_password = generate_password_hash("1234")  # Hashear la contraseña
    if mongo.db.users.find_one({"username": "admin"}) is None:
        mongo.db.users.insert_one({
            "username": "admin",
            "password": hashed_password,  # Contraseña hasheada
            "role": "admin"
        })
        logger.info("Usuario administrador creado exitosamente.")

    # Registrar Blueprints
    from routes.user import user_bp
    from routes.inspection import inspection_bp
    from routes.auth import auth_bp

    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(inspection_bp, url_prefix='/inspection')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    @app.route('/')
    def home():
        logger.info("Solicitud recibida en /")
        return "Backend funcionando", 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)  # Forzar debug
