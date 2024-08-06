"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)


familia_jackson = FamilyStructure("Jackson")


@app.route('/members', methods=['GET'])
def obtener_miembros():
    miembros = familia_jackson.obtener_todos_los_miembros()
    return jsonify(miembros), 200


@app.route('/member/<int:miembro_id>', methods=['GET'])
def obtener_miembro(miembro_id):
    miembro = familia_jackson.obtener_miembro(miembro_id)
    if miembro:
        return jsonify(miembro), 200
    return jsonify({"error": "Miembro no encontrado"}), 404


@app.route('/member', methods=['POST'])
def agregar_miembro():
    datos = request.json
    nuevo_miembro = familia_jackson.agregar_miembro(datos)
    if nuevo_miembro:
        return jsonify(nuevo_miembro), 201
    return jsonify({"error": "Datos inválidos, debe incluir primer_nombre, edad y numeros_de_suerte"}), 400



@app.route('/member/<int:miembro_id>', methods=['DELETE'])
def eliminar_miembro(miembro_id):
    resultado = familia_jackson.eliminar_miembro(miembro_id)
    if resultado.get("done"):
        return jsonify(resultado), 200
    return jsonify({"error": "Miembro no encontrado"}), 404



if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)