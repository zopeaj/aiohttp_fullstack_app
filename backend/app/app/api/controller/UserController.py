import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ["FILE_PATH"]
sys.path.append(path)

from app.core.business.concretes.AuthManager import authManager
from aiohttp.web import RouteTableDef, json_response, Response

userroutes = RouteTableDef()

@userroutes.get("/user/{user_id}")
async def getUser(request):
    pass

@userroutes.put("/user/{user_id}")
async def updateUser(request):
    pass

@userroutes.delete("/user/{user_id}")
async def deleteUser(request):
    pass


