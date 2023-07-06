from flask import request
from flask_api import status


def getMultipleNames():
    data = request.get_json()
    list = data.get("patients", [])
    bind_ids = [":" + str(i + 1) for i in range(len(list))]

    sql = (
        "SELECT DISTINCT(nm_paciente), cd_paciente FROM VW_PACIENTES WHERE cd_paciente IN  (%s)"
        % (",".join(bind_ids))
    )
    names = []
    found = []

    connection = pool.acquire()
    cursor = connection.cursor()
    for result in cursor.execute(sql, list):
        found.append(result[1])
        names.append({"status": "success", "idPatient": result[1], "name": result[0]})

    for idPatient in list:
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
