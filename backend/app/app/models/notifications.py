import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.envron['FILE_PATH']
sys.path.append(path)

from app.db.base_class import Base

class Notification(Base):
    pass

