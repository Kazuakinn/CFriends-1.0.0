import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/collect_followers', methods=['POST'])
def collect_followers():
    username = request.json.get('username')
    # Lógica para coletar seguidores usando a API do Instagram
    return jsonify({"message": "Lista de seguidores coletada."})

@app.route('/add_close_friends', methods=['POST'])
def add_close_friends():
    follower_ids = request.json.get('follower_ids')
    # Lógica para adicionar seguidores aos 'Close Friends'
    return jsonify({"message": "Seguidores adicionados aos 'Close Friends'."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
