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

# Crear el objeto de la familia Jackson
familia_jackson = FamilyStructure("Jackson")

# Obtén todos los miembros de la familia.
@app.route('/members', methods=['GET'])
def obtener_miembros():
    miembros = familia_jackson.obtener_todos_los_miembros()
    return jsonify(miembros), 200

#Recupera un miembro específico de la familia por su ID.
@app.route('/member/<int:miembro_id>', methods=['GET'])
def obtener_miembro(miembro_id):
    miembro = familia_jackson.obtener_miembro(miembro_id)
    if miembro:
        return jsonify(miembro), 200
    return jsonify({"error": "Miembro no encontrado"}), 404


#Añade un nuevo miembro a la familia.
@app.route('/member', methods=['POST'])
def agregar_miembro():
    datos = request.json
    nuevo_miembro = familia_jackson.agregar_miembro(datos)
    if nuevo_miembro:
        return jsonify(nuevo_miembro), 201
    return jsonify({"error": "Datos inválidos, debe incluir primer_nombre, edad y numeros_de_suerte"}), 400


# Elimina un miembro de la familia por su ID.
@app.route('/member/<int:miembro_id>', methods=['DELETE'])
def eliminar_miembro(miembro_id):
    resultado = familia_jackson.eliminar_miembro(miembro_id)
    if resultado:
        return jsonify({"hecho": True}), 200
    return jsonify({"error": "Miembro no encontrado"}), 404

# Iniciar la aplicación si se ejecuta directamente el script
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)