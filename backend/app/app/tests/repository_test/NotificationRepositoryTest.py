import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ['FILE_PATH']
sys.path.append(path)


from testtool import TestCase
from app.crud.repository.notificationRepository import NotificationRepository
from app.models.notifications import Notification
from app.models.user import User


class NotificationRepositoryTests(TestCase):
    def setUp(self):
        self.notificationRepositoryUnderTest = NotificationRepository()

    def test_create_notification(self):
        pass

    def test_update_notification_by_id(self):
        pass

    def test_delete_notification_by_id(self):
        pass


