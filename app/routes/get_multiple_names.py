from sqlalchemy import text
from flask import request
from flask_api import status
from connections import engine, MULTI_QUERY


def get_multiple_names():
    data = request.get_json()
    ids_list = data.get("patients", [])
    bind_ids = [":" + str(i + 1) for i in range(len(ids_list))]
    dict_keys = [str(i + 1) for i in range(len(ids_list))]

    names = []
    found = []

    with engine.connect() as connection:
        result = connection.execute(
            text(MULTI_QUERY.format(",".join(bind_ids))),
            dict(zip(dict_keys, ids_list)),
        )
        for row in result:
            found.append(row[1])
            names.append({"status": "success", "idPatient": row[1], "name": row[0]})

    for id_patient in ids_list:
        if id_patient not in found:
            names.append(
                {
                    "status": "error",
                    "idPatient": id_patient,
                    "name": "Paciente " + str(id_patient),
                }
            )

    return names, status.HTTP_200_OK
