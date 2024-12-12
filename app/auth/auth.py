from flask import Flask, request, jsonify
import hashlib
import requests  # Для взаимодействия с сервисом logs

app = Flask(__name__)

# Пример заранее созданных пользователей
USERS = {
    "user1": hashlib.sha256("password1".encode()).hexdigest(),
    "user2": hashlib.sha256("password2".encode()).hexdigest(),
}

LOGGING_SERVICE_URL = "http://logs:5002/log"  # URL сервиса логирования

def log_action(username, action):
    """Отправка данных в сервис логирования."""
    try:
        response = requests.post(
            LOGGING_SERVICE_URL,
            json={"username": username, "action": action},
            timeout=2  # Ограничение времени ожидания
        )
        if response.status_code != 201:
            app.logger.warning(f"Failed to log action: {response.status_code} {response.text}")
    except requests.RequestException as e:
        app.logger.error(f"Error logging action: {e}")

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if USERS.get(username) == hashed_password:
        log_action(username, "login_success")
        return jsonify({"message": "Login successful!"}), 200
    else:
        log_action(username, "login_failed")
        return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
