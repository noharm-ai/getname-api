from routes.hello import hello
from routes.getName import getName
from routes.getMultipleNames import getMultipleNames
from flask_api import FlaskAPI
from flask_cors import CORS
from connections import FLASK_PORT


app = FlaskAPI(__name__)
CORS(app)

app.add_url_rule("/", view_func=hello)
app.add_url_rule("/patient-name/<int:idPatient>", view_func=getName, methods=["GET"])
app.add_url_rule("/patient-name/multiple", view_func=getMultipleNames, methods=["POST"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=FLASK_PORT, ssl_context="adhoc")
