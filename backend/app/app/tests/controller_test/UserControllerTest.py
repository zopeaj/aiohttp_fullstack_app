from testtool import TestCase
from aiohttp.test import TestClient

class UserControllerTests(TestCase):
    def setUp(self):
        self.client = TestClient()

    def test_create_user(self):
        pass

    def test_read_user(self):
        pass

    def test_get_users_superuser_me(self):
        pass

    def test_get_users_normal_user_me(self):
        pass

    def test_create_user_new_email(self):
        pass

    def test_get_existing_user(self):
        pass

    def test_create_user_existing_username(self):
        pass

    def test_create_user_by_normal_user(self):
        pass

    def test_retrieve_users(self):
        pass

