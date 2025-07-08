from http import HTTPStatus
from fastapi import Request, HTTPException
from starlette.responses import JSONResponse


class GeneralException(HTTPException):
    def __init__(self, detail: str, status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR):
        self.detail = detail
        self.status_code = status_code if status_code >= 400 else HTTPStatus.INTERNAL_SERVER_ERROR


async def exception_handler(request: Request, exception: GeneralException):
    return JSONResponse(
        status_code=exception.status_code,
        content=exception.detail
    )


async def validation_exception_handler(request: Request, exception: str):
    return JSONResponse(
        str(exception),
        status_code=HTTPStatus.BAD_REQUEST
    )


async def no_result_found_exception_handler(request: Request, exception: str):
    return JSONResponse(
        "Forbidden",
        status_code=HTTPStatus.FORBIDDEN
    )
