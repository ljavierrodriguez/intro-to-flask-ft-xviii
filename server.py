from flask import Flask, jsonify, request

import json

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'


@app.route('/', methods=['GET', 'POST'])
def main():

    persona = {
        "id": 1,
        "name": "John",
        "lastname": "Doe"
    }

    return jsonify(persona), 404

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"msg": "Ingresando por el method: " + request.method }), 200

@app.route('/users', methods=['POST'])
def create_user():
    return jsonify({"msg": "Ingresando por el method: " + request.method }), 200

@app.route('/users', methods=['PUT'])
def update_user():
    return jsonify({"msg": "Ingresando por el method: " + request.method }), 200

@app.route('/users', methods=['DELETE'])
def delete_user():
    return jsonify({"msg": "Ingresando por el method: " + request.method }), 200


@app.route('/posts', methods=['GET', 'POST', 'PUT', 'DELETE'])
def posts():
    if request.method == 'GET':
        return jsonify({"msg": "Ingresando por el method: " + request.method }), 200
    if request.method == 'POST':
        return jsonify({"msg": "Ingresando por el method: " + request.method }), 200
    if request.method == 'PUT':
        return jsonify({"msg": "Ingresando por el method: " + request.method }), 200
    if request.method == 'DELETE':
        return jsonify({"msg": "Ingresando por el method: " + request.method }), 200


@app.route('/api/category/<category>/<title>', methods=['GET'])
def category(category, title):

    # fullpath: /category/cat40052/prueba?date=2023-01-10&page=1

    # Recibir datos por query_string ejem: ?date=2023-01-10&page=1
    query = request.args
    date = request.args.get('date')
    page = request.args.get('page')
    print(query['date'],"->", date)
    print(query['page'],"->", page)

    # Recibir datos en el endpoint o ruta ejem: /category/cat40052/prueba
    endpoint = {
        "category": category,
        "title": title
    }

    return jsonify(endpoint), 200

@app.route('/api/category/<category>/<title>', methods=['POST'])
def enviando_datos_por_post(category, title):

    # fullpath: /category/cat40052/prueba

    # Recibir datos en el endpoint o ruta ejem: /category/cat40052/prueba
    endpoint = {
        "category": category,
        "title": title
    }
    """
    # Sin archivos adjuntos  recibimos JSON
    body = request.data # rebimos un string de la data 
    print(body) # mostramos el string tal cual lo recibimos
    parse_body = json.loads(body) # tranformamos el string en un diccionario de python
    print(parse_body) # mostramos el diccionario tal cual esta
    print(parse_body['name']) # accedemos al atributo del diccionario que queremos

    body = request.get_json()
    print(body)
    print(body['name'])

    name = request.json.get('name')
    lastname = request.json.get('lastname')

    print(name)
    print(lastname)
    """

    # recibir datos con form-data (Con archivos adjuntos recibimos si lo necesitamos)

    name = request.form['name']
    lastname = request.form['lastname']

    print(name)
    print(lastname)

    avatar = request.files['avatar']

    print(avatar.filename)

    return jsonify(endpoint), 200






if __name__ == '__main__':
    app.run()




