from dotenv import load_dotenv
from sqlalchemy import URL, create_engine
from urllib.parse import quote
import os

# Get env variables
load_dotenv()

FLASK_PORT = os.getenv("FLASK_PORT")

TYPE = os.getenv("DB_TYPE")
HOST = os.getenv("DB_HOST")
DATABASE = os.getenv("DB_DATABASE")
PORT = os.getenv("DB_PORT")
USER = os.getenv("DB_USER")
PASS = quote(str(os.getenv("DB_PASS")))

# Pool parameters
POOL_SIZE = os.getenv("POOL_SIZE")
POOL_MAX = os.getenv("POOL_MAX_OVERFLOW")
POOL_TIMEOUT = os.getenv("POOL_TIMEOUT")

QUERY = os.getenv("DB_QUERY")
MULTI_QUERY = os.getenv("DB_MULTI_QUERY")
NAME_QUERY = os.getenv("DB_NAME_QUERY")

# JWT
JWT_SECRET = os.getenv("JWT_SECRET")

if TYPE == "oracle":
    url_object = (
        f"oracle+cx_oracle://{USER}:{PASS}@{HOST}:{PORT}/?service_name={DATABASE}"
    )

elif TYPE == "firebird":
    url_object = f"firebird+fdb://{USER}:{PASS}@{HOST}:{PORT}/{DATABASE}"

elif TYPE == "mysql":
    url_object = f"mysql+pymysql://{USER}:{PASS}@{HOST}:{PORT}/{DATABASE}"

else:
    TYPE = "mssql+pymssql" if TYPE == "mssql" else TYPE
    url_object = URL.create(
        TYPE, username=USER, password=PASS, host=HOST, database=DATABASE, port=PORT
    )

engine = create_engine(
    url_object,
    pool_size=int(POOL_SIZE),
    max_overflow=int(POOL_MAX),
    pool_timeout=int(POOL_TIMEOUT),
    pool_pre_ping=True,
    pool_recycle=3600,
)
