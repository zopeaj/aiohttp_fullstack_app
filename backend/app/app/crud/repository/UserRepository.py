import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ['FILE_PATH']
sys.path.append(path)

from app.models.user import User
from app.db.get_db import get_db
from fastapi import Depends
from sqlalchemy.orm import Session

class UserRepository:
    def __init__(self):
        self.db: Session = Depends(get_db)

    def save(self):
        pass

    def update(self):
        pass

    def remove(self):
        pass

    def getById(self):
        pass



