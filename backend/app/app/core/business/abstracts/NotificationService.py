import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ['FILE_PATH']
sys.path.append(path)


class NotificationService:
    def __init__(self, notificationRepository):
        self.notificationRepository = notificationRepository

