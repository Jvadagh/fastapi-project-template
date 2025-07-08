from sqlalchemy.ext.asyncio import AsyncSession


class ExampleService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @staticmethod
    async def get_example_dictionary(pagination) -> dict:
        return {"title": f"example with {pagination}"}
