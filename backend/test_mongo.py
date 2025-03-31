from pymongo import MongoClient

uri = "mongodb://172.19.255.201:27017/sistema_monitoreo"
try:
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)  # Timeout de 5 segundos
    client.server_info()  # Fuerza una conexión real
    print("Conexión a MongoDB exitosa!")
    print("Bases de datos disponibles:", client.list_database_names())
except Exception as e:
    print("Error al conectar a MongoDB:", str(e))