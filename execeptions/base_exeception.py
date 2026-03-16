from fastapi import Request
from fastapi.responses import JSONResponse
from execeptions.app_exeception import AppExeception


def base_exeception_handler(request: Request, exc: Exception):
    if isinstance(exc, AppExeception):
        status_code = exc.status_code
        message = exc.message
    else:
        status_code = 500
        message = str(exc)

    return JSONResponse(status_code=status_code, content=message)
