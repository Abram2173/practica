from werkzeug.security import generate_password_hash

# Hashear la contraseña "1234"
hashed_password = generate_password_hash("1234")

print(hashed_password)
