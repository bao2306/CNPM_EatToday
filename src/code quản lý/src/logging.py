from fastapi import HTTPException
from fastapi.responses import JSONResponse

def add_error_handlers(app):
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request, exc):
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})