from flask_api import status


def getName(idPatient):
    name = None

    # with cx_Oracle.connect("user", "pass", "127.0.0.1:1521/service") as connection:
    connection = pool.acquire()
    cursor = connection.cursor()
    for result in cursor.execute(
        "SELECT nm_paciente FROM schema.paciente WHERE cd_paciente = " + str(idPatient)
    ):
        name = result[0]

    pool.release(connection)

    if name:
        return {
            "status": "success",
            "idPatient": idPatient,
            "name": name,
        }, status.HTTP_200_OK
    else:
        return {
            "status": "error",
            "idPatient": idPatient,
            "name": "Paciente " + str(idPatient),
        }, status.HTTP_400_BAD_REQUEST
