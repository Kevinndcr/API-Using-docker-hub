# Import required libraries
import locale
from flask import Flask, jsonify, abort, make_response, request

import json

# Create default flask application
#locale.setlocale(locale.LC_ALL, "es")
app = Flask(__name__)

datos = {}

# -----------------------------------------------------
# Error support section
# -----------------------------------------------------
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request....!'}), 400)

@app.errorhandler(401)
def unauthorized(error):
    return make_response(jsonify({'error': 'Unauthorized....!'}), 401)

@app.errorhandler(403)
def forbiden(error):
    return make_response(jsonify({'error': 'Forbidden....!'}), 403)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found....!'}), 404)

@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify({'error': 'Internal server error....!'}), 500)


# Get data student
@app.route('/estudiante', methods=['GET'])
def get_estu():
    salida = {
        'status':200,
        'status_message': 'OK',
        'estudiante': {
            'id': 101110111,
            'nombre': 'Morticia',
            'apellidos': 'Addams Frug',
            'nivel': 'Doctorado Psicologia Inversa',
            'email': 'maddamsf@gmail.com',
            'celular': '300 111 1111'
        }
    }
    return jsonify({'datos': salida}), 200

@app.route('/estadisticas', methods=['GET'])
def get_esta():
    global datos
    ldat = []
    try:
        for dt in datos:
            ldat.append(datos.get(dt))

        salida = {
            'status': 200,
            'status_message': 'OK',
            'datos': datos,
            'estadisticas': {
                'nValores': len(ldat),
                'menor': min(ldat),
                'mayor': max(ldat),
                'suma': sum(ldat),
                'promedio': (sum(ldat) / len(ldat))
            }
        }
        return jsonify({'resultado': salida}), 200
    except Exception as excp:
        abort(500)

@app.route('/elevar', methods=['GET'])
def get_eleva():
    global datos
    ldat = {}
    for dt in datos:
        ldat[dt] = (datos[dt]*datos[dt])

    salida = {
        'status': 200,
        'status_message': 'OK',
        'd_originales': datos,
        'd_elevados': ldat
    }
    return jsonify({'resultado': salida}), 200


@app.route('/elevar/<int:pot>', methods=['GET'])
def get_eleva2(pot):
    global datos
    ldat = {}
    for dt in datos:
        ldat[dt] = (pow(datos[dt], pot))

    salida = {
        'status': 200,
        'status_message': 'OK',
        'd_originales': datos,
        'd_elevados': ldat
    }
    return jsonify({'resultado': salida}), 200


@app.route('/datos', methods=['POST'])
def post_datos():
    if not request.json:
        abort(400)
    else:
        global datos
        datos = json.dumps(request.json)
        datos = json.loads(datos)

        canti = len(datos)
        salida = {
            'status': 201,
            'status_message': 'Data created',
            'datos': {
                'nValores': canti
            }
        }
    return jsonify({'resultado': salida}), 201


# -----------------------------------------------------
# Create thread app
# -----------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

