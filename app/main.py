from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status
from flask_cors import CORS
import psycopg2
from psycopg2 import pool

app = FlaskAPI(__name__)
CORS(app)

pool = psycopg2.pool.SimpleConnectionPool(
                                        1,
                                        20,
                                        user="user",
                                        password="pass",
                                        host="host",
                                        port="5432",
                                        database="database")

@app.route("/")
def hello():
    return "Serviço de nomes habilitado! Volte para a NoHarm e use o sistema normalmente ;)"

@app.route("/patient-name/<int:idPatient>", methods=['GET'])
def getRawName(idPatient):
    name = None
    
    connection = pool.getconn()
    cursor = connection.cursor()
    cursor.execute("SELECT nome FROM public.usuario WHERE idusuario = %(idPatient)s", {'idPatient': idPatient})
    for result in cursor.fetchall():
        name = result[0]

    cursor.close()
    pool.putconn(connection)

    if name:
        return {
            'status': 'success',
            'idPatient': idPatient,
            'name': name
        }, status.HTTP_200_OK
    else:
        return {
            'status': 'error',
            'idPatient': idPatient,
            'name': 'Paciente ' + str(idPatient)
        }, status.HTTP_400_BAD_REQUEST


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=443, ssl_context='adhoc')
