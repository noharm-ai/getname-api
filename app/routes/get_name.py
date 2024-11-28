from sqlalchemy import text
from flask_api import status
from resources.connections import engine, QUERY
from resources.cache import cache
from resources.api_decorator import api_endpoint


@api_endpoint()
@cache.cached()
def get_name(idPatient):
    name = None
    with engine.connect() as connection:
        result = connection.execute(
            text(QUERY.format(":idPatient")), {"idPatient": idPatient}
        )
        for row in result:
            name = row[0]
            data = {key: value for key, value in row._mapping.items()}

    if name:
        return {
            "status": "success",
            "idPatient": idPatient,
            "name": name,
            "data": data,
        }, status.HTTP_200_OK
    else:
        return {
            "status": "error",
            "idPatient": idPatient,
            "name": "Paciente " + str(idPatient),
            "data": {},
        }, status.HTTP_400_BAD_REQUEST
