from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status
from model import db, Patient
from flask_cors import CORS
import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

app = FlaskAPI(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://user:pass@127.0.0.1:1521/service'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
CORS(app)

@app.route("/")
def hello():
    return "Hello World from Flask"

@app.route("/patient-name/<int:idPatient>", methods=['GET'])
def getName(idPatient):

    p = Patient.query.get(idPatient)

    if p:
        return {
            'status': 'success',
            'idPatient': idPatient,
            'name': p.name
        }, status.HTTP_200_OK
    else:
        return {
            'status': 'error',
            'idPatient': idPatient,
            'name': 'Paciente ' + str(idPatient)
        }, status.HTTP_400_BAD_REQUEST

@app.route("/patient-raw/<int:idPatient>", methods=['GET'])
def getRawName(idPatient):

    name = None
    
    with cx_Oracle.connect("user", "pass", "127.0.0.1:1521/service") as connection:
        cursor = connection.cursor()
        for result in cursor.execute("SELECT nm_paciente FROM schema.paciente WHERE cd_paciente = "+str(idPatient)):
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