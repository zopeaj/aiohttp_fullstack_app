import os
import sys
from dotenv import load_dotenv
load_dotenv()



from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt


from app.config.settings.settingConfiguration settings


class JWTConfig:
    def __init__(self):
        self.algorithm: str =
        self.secret_key: str =

    def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
        pass

    def verify_access_token():
        pass


