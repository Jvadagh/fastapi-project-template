from http import HTTPStatus
from fastapi import Request, Response

from app.core.config import settings


async def maintenance_middleware(request: Request, call_next) -> Response:
    if settings.MAINTENANCE_MODE:
        return Response("Service_unavailable", status_code=HTTPStatus.SERVICE_UNAVAILABLE)
    return await call_next(request)
