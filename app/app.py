from fastapi import FastAPI
from app.api.routers import api_router
from sqlalchemy.exc import NoResultFound
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.middlewares.app_middlewares import maintenance_middleware
from app.middlewares.exception_handlers import (
    validation_exception_handler,
    exception_handler,
    no_result_found_exception_handler,
    GeneralException
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

if settings.ENVIRONMENT != "DEVELOPMENT":
    app.exception_handler(ValueError)(validation_exception_handler)
    app.exception_handler(NoResultFound)(no_result_found_exception_handler)
    app.exception_handler(GeneralException)(exception_handler)

app.include_router(api_router, prefix="/api")

app.middleware('http')(maintenance_middleware)
