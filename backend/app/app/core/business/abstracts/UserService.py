import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ['FILE_PATH']
sys.path.append(path)

class UserService:
    def __init__(self, userRepository):
        self.userRepository = userRepository

    def create(self):
        pass

    def update(self):
        pass

    def getById(self):
        pass

    def delete(self):
        pass

