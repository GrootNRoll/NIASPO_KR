from flask import Flask, request, jsonify
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



# Настройки подключения к базе данных
DB_CONFIG = {
    'dbname': 'corporate_db',
    'user': 'admin',
    'password': 'password',
    'host': 'database',  # Название контейнера базы данных
    'port': 5432
}

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

@app.route('/data', methods=['GET'])
def get_data():
    """Получить данные из таблицы some_table"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM some_table;")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(results)

@app.route('/data', methods=['POST'])
def add_data():
    """Добавить данные в таблицу some_table"""
    data = request.json
    if 'field1' not in data or 'field2' not in data:
        return jsonify({"error": "Missing fields"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO some_table (field1, field2) VALUES (%s, %s)", 
                   (data['field1'], data['field2']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Data added successfully!"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
