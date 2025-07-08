from fastapi import APIRouter

from app.api.endpoints.example_endpoints import example_endpoints

api_router = APIRouter()

api_router.include_router(example_endpoints, prefix='/example-endpoints')
