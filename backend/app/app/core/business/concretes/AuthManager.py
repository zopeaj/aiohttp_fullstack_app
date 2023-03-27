import os
import sys

path = os.environ['FILE_PATH']
sys.path.append(path)

from app.core.business.concretes.EmailSenderService import EmailSenderService
from app.core.business.abstracts.UserService import UserService
from app.core.business.abstracts.NotificationService import NotificationService
from app.config.security.jwt.jwtConfig import JwtConfig


class AuthManager:
    def __init__(self, userService, emailSenderService, jwtConfig, notificationService):
        self.userService = userService
        self.emailSenderService = emailSenderService
        self.jwtConfig = jwtConfig
        self.notificationService = notificationService

    def register(self):
        pass

    def confirm(self):
        pass


authManager = AuthManager(UserService(), EmailSenderService(), JwtConfig(), NotificationService())
