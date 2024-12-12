from flask import Flask, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

# Путь к файлу для хранения логов
LOG_FILE = "logs.json"

# Функция для загрузки логов из файла
def load_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []  # Если файл пустой или поврежден
    return []

# Функция для сохранения логов в файл
def save_logs():
    with open(LOG_FILE, "w") as file:
        json.dump(LOGS, file, indent=4)

# Загружаем логи при старте приложения
LOGS = load_logs()

@app.route('/log', methods=['POST'])
def log_event():
    data = request.json
    username = data.get('username')
    action = data.get('action')  # Например, "login", "logout"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not username or not action:
        return jsonify({"error": "Username and action are required"}), 400

    log_entry = {
        "username": username,
        "action": action,
        "timestamp": timestamp
    }
    LOGS.append(log_entry)
    save_logs()  # Сохраняем в файл
    return jsonify({"message": "Log recorded successfully!"}), 201

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(LOGS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
