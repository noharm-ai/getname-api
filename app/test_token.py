import jwt
import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")

token = jwt.encode(
    payload={
        "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=5),
        "iss": "noharm",
    },
    key=JWT_SECRET,
)

print(token)
