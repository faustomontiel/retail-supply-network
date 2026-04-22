import datetime as dt
from src.config.config import JWT_KEY
import jwt


class Security():
    def __init__(self):
        self._jwtkey = JWT_KEY

    def generate_token(self):
        payload = {
            'iat': dt.datetime.now(),
            'exp': dt.datetime.now() + dt.timedelta(minutes=5)
        }

        return jwt.encode(payload, self._jwtkey, algorithm="HS256")
