#Flask library
from flask import Blueprint
from flask import jsonify
from flask import request
from Services.Usuarios.usuarios import users

#HTTP library
from http import HTTPStatus

v1 = Blueprint("version1", "version1", url_prefix="/v1")

@v1.route('/conexionDB', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def registro():
    
    if request.method == 'POST':
        json_data = request.get_json()
        response = users(json_data).crear_documento()
        return jsonify(response), HTTPStatus.OK

    if request.method == 'GET':
        json_data = request.get_json()
        response = users(json_data).buscar_documento()
        return jsonify({'registros':response}), HTTPStatus.OK
    
    if request.method == 'PUT':
        json_data = request.get_json()
        response = users(json_data).actualizar_documento()
        return jsonify(response), HTTPStatus.OK
    
    if request.method == 'DELETE':
        json_data = request.get_json()
        response = users(json_data).borrar_documento()
        return jsonify(response), HTTPStatus.OK
