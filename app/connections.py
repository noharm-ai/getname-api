def client(conn_string):
    pool = None

    if conn_string == "postgres":
        import psycopg2

        pool = 1
    elif conn_string == "oracle":
        import cx_Oracle

        pool = 2
    elif conn_string == "mssql":
        import msserver

        pool = 3
    return pool
