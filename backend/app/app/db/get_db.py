import os
import sys
from dotenv import load_dotenv

load_dotenv()

path = os.environ['FILE_PATH']
sys.path.append(path)

from app.db.base_class import Base
from app.db.session import SessionLocal

def get_db() -> None:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

