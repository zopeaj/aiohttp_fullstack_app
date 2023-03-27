import os
import sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ["FILE_PATH"]
sys.path.append(path)

from app.api.controller.AuthController import authroutes
from app.api.controller.UserController import userroutes

def setup_routes(app):
    app.add_routes(authroutes)
    app.add_routes(userroutes)

