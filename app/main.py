from routes.hello import hello
from routes.get_name import get_name
from routes.get_multiple_names import get_multiple_names
from flask_api import FlaskAPI
from flask_cors import CORS


app = FlaskAPI(__name__)
CORS(app)

app.add_url_rule("/", view_func=hello)
app.add_url_rule("/patient-name/<int:idPatient>", view_func=get_name, methods=["GET"])
app.add_url_rule(
    "/patient-name/multiple", view_func=get_multiple_names, methods=["POST"]
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", ssl_context="adhoc")
