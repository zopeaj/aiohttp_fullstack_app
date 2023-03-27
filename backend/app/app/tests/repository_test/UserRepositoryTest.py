import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ['FILE_PATH']
sys.path.append(path)

from testtool import TestCase
from app.crud.repository.crud.UserRepository import UserRepository
from app.models.user import User


class UserRepositoryTests(TestCase):
    def setUp(self):
        self.userRepositoryUnderTests = UserRepository()

    def test_create_user(self):
        pass

    def test_update_user(self):
        pass

    def test_delete_user_by_id(self):
        pass

    def test_get_user(self):
        pass

    def test_check_if_user_is_active(self):
        pass

    def test_check_if_user_is_active_inactive(self):
        pass

    def test_check_if_user_is_superuser_normal_user(self):
        pass
