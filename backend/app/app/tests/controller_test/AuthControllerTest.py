from testtool import TestCase
from aiohttp.test import TestClient


class AuthControllerTests(TestCase):
    def setUp(self):
        self.client = TestClient()

    def test_get_access_token(self):
        pass

    def test_use_access_token(self):
        pass

