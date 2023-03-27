import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ['FILE_PATH']
sys.path.append(path)

from app.db.base import Base
from sqlalchemy import String, Integer, Sequence


class User(Base):
    pass

