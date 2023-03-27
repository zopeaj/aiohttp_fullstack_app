import os
import sys
from dotenv import load_dotenv
load_dotenv()

from passlib.context import CryptContext

class BCryptPasswordConfiguration:
    def __init_(self, ):
        self.pwd_context = CryptContext(scheme=["bcrypt"])

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)
