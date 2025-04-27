# api_json_server.py
from flask import Flask, jsonify
import json

app = Flask(__name__)

# Cargamos el archivo JSON al iniciar
with open('db.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Ruta principal para leer la base
@app.route('/leer_base', methods=['GET'])
def leer_base():
    return jsonify(data)

# Puedes agregar más rutas si quieres filtrar, buscar, etc.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
