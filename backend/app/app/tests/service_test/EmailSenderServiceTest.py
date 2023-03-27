from testtool import TestCase
from app.models.user import User
from app.core.business.core.abstracts.UserService import UserService
from app.crud.repository.UserRepository import UserRepository

class EmailSenderServiceTest(TestCase):
    def setUp(self):
        self.userServiceUnderTest = UserService(UserRepository())

    def test_send_email_to_registered_user(self):
        pass

    def test_send_email_to_password_recovery(self):
        pass

    def test_send_email_to_changed_password(self):
        pass


