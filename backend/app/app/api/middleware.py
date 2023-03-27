from aiohttp import web

@web.middleware
async def error_middleware(request, handler):
    try:
        response = await handler(request)
        if response.status != 400:
            return response
        message = response.message
    except web.HTTPException as ex:
        if ex.status != 404:
            raise
        message = ex.reason
    return web.json_response({'error':message})
