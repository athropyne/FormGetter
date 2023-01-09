from fastapi import APIRouter

from tests.database_text_query import TestQuery
from tests.examples_pattern_form import ExamplesPatternForm

test_router = APIRouter(prefix="/test")


@test_router.get("/FillDatabase")
async def fill_database():
    await clear_database()
    await TestQuery.fill_database(await ExamplesPatternForm.get_pattern_list())
    return "база данных успешно создана и заполнена"


@test_router.get("/ClearDatabase")
async def clear_database():
    await TestQuery.clear_database()
    return "база данных очищена"


