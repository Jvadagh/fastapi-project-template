from http import HTTPStatus
from typing import Annotated
from fastapi import APIRouter, Depends

from app.api.dependencies.base import PaginationParam, pagination_param
from app.api.schemas.example_schemas import ExampleViewModel
from app.services.example_service import ExampleService
from app.services.factory import example_service_factory

example_endpoints = APIRouter(tags=["Examples"])


@example_endpoints.get(path="/example", response_model=ExampleViewModel, status_code=HTTPStatus.OK)
async def retrieve_dictionary(
        action_service: Annotated[ExampleService, Depends(example_service_factory)],
        pagination: Annotated[PaginationParam, Depends(pagination_param)],
) -> dict:
    return await action_service.get_example_dictionary(pagination=pagination)
