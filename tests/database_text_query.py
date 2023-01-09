from core.db import DB


class TestQuery:
    @staticmethod
    async def fill_database(patterns: list[dict]):
        DB.insert_multiple(patterns)

    @staticmethod
    async def clear_database():
        DB.truncate()
