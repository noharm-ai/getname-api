from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status
from flask_cors import CORS
from functools import lru_cache
import pymssql

app = FlaskAPI(__name__)
CORS(app)

connection = pymssql.connect(server='server', user='user', 
                             password='password', 
                             database='database')

@app.route("/")
def hello():
    return "Servico de nomes habilitado! Volte para a NoHarm e use o sistema normalmente ;)"

#@lru_cache(maxsize=1024)
@app.route("/patient-name/<int:idPatient>", methods=['GET'])
def getRawName(idPatient):

    name = None

    cursor = connection.cursor()
    cursor.execute("SELECT PAC_NOME FROM SMART.DBO.PAC WHERE PAC_REG = "+str(idPatient))
    result = cursor.fetchone()
    name = result[0]

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
