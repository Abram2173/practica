import pytest
from app import create_app, mongo

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    # Limpiar las colecciones antes de cada prueba
    with app.app_context():
        mongo.db.users.drop()
        mongo.db.inspections.drop()

    with app.test_client() as client:
        yield client


def test_add_user(client):
    response = client.post('/users', json={"username": "testuser"})
    assert response.status_code == 201
    assert response.json == {"message": "Usuario agregado exitosamente"}

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_inspection(client):
    response = client.post('/inspections', json={"inspection_data": "testdata"})
    assert response.status_code == 201
    assert response.json == {"message": "Inspección agregada exitosamente"}

def test_add_user_missing_username(client):
    response = client.post('/users', json={})  # Sin username
    assert response.status_code == 400
    assert response.json == {"error": "El nombre de usuario es requerido"}

def test_get_inspections(client):
    response = client.get('/inspections')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_register_user(client):
    response = client.post('/register', json={"username": "newuser", "password": "12345"})
    assert response.status_code == 201
    assert response.json == {"message": "Usuario registrado exitosamente"}

def test_login_user(client):
    # Primero registra un usuario
    client.post('/register', json={"username": "newuser", "password": "12345"})
    # Luego intenta iniciar sesión
    response = client.post('/login', json={"username": "newuser", "password": "12345"})
    assert response.status_code == 200
    assert response.json == {"message": "Login exitoso"}