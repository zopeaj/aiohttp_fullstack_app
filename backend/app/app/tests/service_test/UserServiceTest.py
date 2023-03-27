import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ['FILE_PATH']
os.path.append(path)

from testtool import TestCase
from app.core.business.abstracts.UserService import UserService
from app.crud.repository.UserRepository import UserRepository
from app.models.user import User
from app.db.get_db import get_db
from fastapi import Depends
from sqlalchemy.orm import Session

class UserServiceTests(TestCase):
    def setUp(self):
        self.userServiceUnderTest = UserService(UserRepository())

    def test_create_user_service(self):
        pass

    def test_update_user_service(self):
        pass

