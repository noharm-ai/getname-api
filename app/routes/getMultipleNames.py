from sqlalchemy import text
from flask import request
from flask_api import status
from connections import engine, MULTI_QUERY


def getMultipleNames():
    print("INTO GET MULTIPLE")
    data = request.get_json()
    ids_list = data.get("patients", [])
    bind_ids = [":" + str(i + 1) for i in range(len(ids_list))]

    sql = MULTI_QUERY.format(",".join(bind_ids))
    names = []
    found = []

    with engine.connect() as connection:
        result = connection.execute(text(sql))
        for row in result:
            found.append(row.name)
            names.append(
                {"status": "success", "idPatient": result[1], "name": result[0]}
            )

    for idPatient in ids_list:
        if str(idPatient) not in found:
            names.append(
                {
                    "status": "error",
                    "idPatient": idPatient,
                    "name": "Paciente " + str(idPatient),
                }
            )

    pool.release(connection)

    return names, status.HTTP_200_OK
