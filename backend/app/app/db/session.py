import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ['FILE_PATH']
sys.path.append(path)

from app.config.settings.settingConfiguration import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



engine = create_engine(settings.POSTGRESDB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)
