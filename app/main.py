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
    
@app.route("/patient-name/multiple", methods=['POST'])
def get_multiple():
    data = request.get_json()
    list = data.get("patients", [])
    bind_ids = [":" + str(i + 1) for i in range(len(list))]

    sql = "SELECT DISTINCT(nm_paciente), cd_paciente FROM VW_PACIENTES WHERE cd_paciente IN  (%s)" % (",".join(bind_ids))
    names = []
    found = []
    
    # TODO: review  mssql
    #connection = pool.acquire()
    cursor = connection.cursor()
    cursor.execute(sql, list):
    records = cursor.fetachall():
    for result in records:
        found.append(result[1])
        names.append({
            'status': 'success',
            'idPatient': result[1],
            'name': result[0]
        })

    for idPatient in list:
        if str(idPatient) not in found:
            names.append({
                'status': 'error',
                'idPatient': idPatient,
                'name': 'Paciente ' + str(idPatient)
            })
            
    #pool.release(connection)

    return names, status.HTTP_200_OK


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=443, ssl_context='adhoc')
