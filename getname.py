from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from flask_sqlalchemy import SQLAlchemy
from models import db, User
from config import Config
from flask_cors import CORS

app = FlaskAPI(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://scott:tiger@127.0.0.1:1521/sidname'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = { "pool_recycle" : 500, "pool_pre_ping": True }

db.init_app(app)
CORS(app)

@app.route("/patient-name/<int:idPatient>", methods=['GET'])
def getName(idPatient):
    return {
        'status': 'success',
        'idPatient': idPatient,
        'name': 'Fulano da Silva e Santos'
    }, status.HTTP_200_OK


if __name__ == "__main__":
    app.run(debug=True)
