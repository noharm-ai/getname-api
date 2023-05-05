from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status
from flask_cors import CORS
from functools import lru_cache
import cx_Oracle

app = FlaskAPI(__name__)
CORS(app)

pool = cx_Oracle.SessionPool(user="user", password="pass",
                             dsn="127.0.0.1:1521/service", min=2,
                             max=5, increment=1)

@app.route("/")
def hello():
    return "Serviço de nomes habilitado! Volte para a NoHarm e use o sistema normalmente ;)"

#@lru_cache(maxsize=1024)
@app.route("/patient-name/<int:idPatient>", methods=['GET'])
def getRawName(idPatient):

    name = None
    
    #with cx_Oracle.connect("user", "pass", "127.0.0.1:1521/service") as connection:
    connection = pool.acquire()
    cursor = connection.cursor()
    for result in cursor.execute("SELECT nm_paciente FROM schema.paciente WHERE cd_paciente = "+str(idPatient)):
        name = result[0]
    
    pool.release(connection)

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
    
    connection = pool.acquire()
    cursor = connection.cursor()
    for result in cursor.execute(sql, list):
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
            
    pool.release(connection)

    return names, status.HTTP_200_OK


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=443, ssl_context='adhoc')
