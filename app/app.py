import string
import secrets
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

def check_password_strength(password):
    if len(password) < 12:
        return False, "A senha deve ter pelo menos 12 caracteres."
    if not re.search(r"[A-Z]", password):
        return False, "A senha deve conter pelo menos uma letra maiúscula."
    if not re.search(r"[a-z]", password):
        return False, "A senha deve conter pelo menos uma letra minúscula."
    if not re.search(r"\d", password):
        return False, "A senha deve conter pelo menos um número."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "A senha deve conter pelo menos um caractere especial."
    return True, "Senha segura!"

def generate_secure_password(length=16):
    # Garante pelo menos um caractere de cada grupo obrigatório
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()"
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        is_valid, _ = check_password_strength(password)
        if is_valid:
            return password

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json() or {}
    password = data.get('password', '')
    
    if not password:
        return jsonify({"error": "O campo 'password' é obrigatório."}), 400
        
    is_secure, message = check_password_strength(password)
    return jsonify({"secure": is_secure, "message": message})

@app.route('/generate', methods=['GET'])
def generate():
    # Permite customizar o tamanho via query string, mantendo o mínimo de 12
    length = request.args.get('length', default=16, type=int)
    if length < 12:
        length = 12
    elif length > 64:
        length = 64
        
    password = generate_secure_password(length)
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)