import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ['FILE_PATH']
sys.path.append(path)

from app.db.base_classe import Base
from app.models.user import User
from app.models.notifications import Notification

