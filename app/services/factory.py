from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database.postgres import get_db


async def example_service_factory(
        session: Annotated[AsyncSession, Depends(get_db)]
) -> object:
    from app.services.example_service import ExampleService
    return ExampleService(session)
