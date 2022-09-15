import pymongo
import certifi
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)

# ca = certifi.where()
# client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.z6feyqq.mongodb.net/bd-registro-academico?retryWrites=true&w=majority")
# db = client.test
# print(db)

# baseDatos = client["bd-registro-academico"]
# print(baseDatos.list_collection_names())


from Controladores.ControladorEstudiante import ControladorEstudiante
miControladorEstudiante=ControladorEstudiante()

@app.route("/estudiantes", methods=['GET'])
def getEstudiantes():
    json = miControladorEstudiante.index()
    return jsonify(json)


@app.route("/estudiantes", methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json = miControladorEstudiante.create(data)
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['GET'])
def getEstudiante(id):
    json = miControladorEstudiante.show(id)
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json = miControladorEstudiante.update(id, data)
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['DELETE'])
def eliminarEstudiante(id):
    json = miControladorEstudiante.delete(id)
    return jsonify(json)


@app.route("/", methods=['GET'])
def test():
    response = {
        "message": "Server running ..."
    }
    return jsonify(response)


def config():
    with open('config.json') as f:
        data = json.load(f)
    return data


# if __name__ == '__main__':
if True:
    dataConfig = config()
    print("Server running : " + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])

