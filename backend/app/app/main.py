import os
import sys
from dotenv import load_dotenv
import logging
load_dotenv()

path = os.environ["FILE_PATH"]
sys.path.append(path)

import aiohttp_cors
from aiohttp import web
from app.api.routes import setup_routes
from app.api.middleware import error_middleware
import aiohttp

app = web.Application()
setup_routes(app)
app.middleware.append(error_middleware)

cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        expose_headers="*" or ("X-Custom-Server-Header"),
        allow_headers="*" or ("X-Requested-With", "Content-Type"),
        max_age=3600,
    ),
    "http://localhost:3000": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        expose_headers="*",
        allow_headers="*",
        max_age=3600
    )
})

for route in list(app.router.routes()):
    cors.add(route)

logging.basicConfig(level=logging.WARN)

web.run_app(app, host="127.0.0.1", port=5051, access_log_class=aiohttp.helpers.AccessLogger, access_log_format=aiohttp.helpers.AccessLogger.LOG_FORMAT, access_log=aiohttp.log.access_logger, handle_signals=True)

