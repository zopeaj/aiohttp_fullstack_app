import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ['FILE_PATH']
sys.path.append(path)

from app.models.notification import Notification
from app.models.user import User
from app.db.get_db import get_db
from sqlalchemy.orm import Session
from fastapi import Depends


class NotificationRepository:
    def __init__(self):
        self.db: Session = Depends(get_db)

    def save(self):
        pass

    def delete(self):
        pass

    def getById(self):
        pass

