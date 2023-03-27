from testtool import TestCase
from app.crud.repository.NotificationRepository import NotificationRepository
from app.core.busines.abstracts.NotificationService import NotificationService

class NotificationServiceTest:
    def setUp(self):
        self.notificationServiceUnderTest = NotificationService(NotificationRepository())

    def test_create_notification_service(self):
        pass
