#!flask/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, request, jsonify, abort

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# yagmail.register(os.environ['USUARIO_EMAIL'], os.environ['PASS_EMAIL'])


@app.route('/', methods=['GET'])
def index():
    info = {
        "mensaje" : "Bienvenides a la API del curriculum vitae de Brenda.",
        "acciones" : [
            "GET /curriculum",
            "POST /mensajes"
        ]
    }
    return jsonify(info)


@app.route('/curriculum', methods=['GET'])
def cv():
    url_imagen = request.host_url + "static/fotoB.jpg"
    cv = {
        "nombre" : "Brenda",
        "apellido" : "Flores",
        "residencia" : "Argentina",
        "experiencia" : [{
            "posicion" : "Soporte de Infraestructura",
            "empresa" : "Gobierno de la Ciudad de Buenos Aires",
            "fecha" : "2019",
            "detalles" : "b"
        },
        {
            "posicion" : "Tester Manual",
            "empresa" : "IBM Argentina",
            "fecha" : "2018",
            "detalles" : "a"
        }],
        "educación" : {
            "nivel" : "Universitario en curso",
            "titulo" : "Licenciatura en Ciencias de la Computacion",
            "institucion" : "UBA",
            "facultad" : "FCEyN"
        },
        "intereses" : ["python", "linux", "networking"],
        "redes" : {
            "github" : "https://github.com/brendasejas",
            "linkedin" : "https://www.linkedin.com/in/brenda-flores-sejas"
        },
        "foto" : url_imagen

    }
    return jsonify(cv)

@app.route('/mensajes', methods=['POST'])
def contacto():
    mensaje = request.get_data()
    if not mensaje:
        abort(400, description="Debe enviar su mensaje en el body del POST.")
    print("MENSAJE DE CONTACTO:" + str(mensaje))
    return "Gracias por su mensaje."


if __name__ == '__main__':
    app.run()