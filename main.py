import urllib.parse

import uvicorn as uvicorn
from fastapi import FastAPI, Body
from starlette.responses import FileResponse

from core import config
from core.db import DB
from routes.test import test_router
from utils.formatter import Formatter
from utils.walidator import Validator

app = FastAPI()

app.include_router(test_router)


@app.get("/")
async def root():
    return FileResponse("public/index.html")


@app.post("/get_form")
async def get_form(data: str = Body()):
    formatted_data = dict(urllib.parse.parse_qsl(data))  # преобразует данные в человеческий вид
    prepared_data = await Formatter.format(formatted_data, Validator)  # форматирует и валидирует входные данные
    form_pattern_from_base = iter(DB)  # получает все документы БД в виде генератора ( спорный момент )
    filtered_patterns = {}  # шаблоны похожие на запрошенную форму ( имеют лишние поля )
    for i in form_pattern_from_base:
        name = i.pop('name')  # вытаскиваем имя шаблона
        if i.items() == prepared_data.items():  # шаблон сошелся полностью
            return name
        if i.items() <= prepared_data.items():  # запрос сошелся с одним или несколькими шаблонами
            filtered_patterns[name] = len(i)  # сохраяем имя шаблона и его размер
    if len(filtered_patterns) == 0:  # если ни один шаблон не совпал с запросом
        return prepared_data
    if config.ONE_PATTERN_ONLY:  # если multipattern отключен
        max_weight = max(filtered_patterns.values())  # определяем размер самого большого из отфильрованных шаблонов
        patterns_with_max_weight = [name
                                    for name, count in filtered_patterns.items()
                                    if filtered_patterns[
                                        name] == max_weight]  # список всех шаблонов с максимальным размером
        if len(patterns_with_max_weight) == 1:  # вернуть если такой шаблон один
            return patterns_with_max_weight[0]
        if len(patterns_with_max_weight) > 1:  # вернуть динамически сгенерированный шаблон (конфликт фильтрации)
            return prepared_data
    else:  # если включен возвращаем список всех подходящих шаблонов
        all_filtered_patterns = [i for i in filtered_patterns.keys()]
        if len(all_filtered_patterns) == 1:
            return all_filtered_patterns[0]
        return all_filtered_patterns


if __name__ == "__main__":
    uvicorn.run(app="main:app",
                host=config.HOST,
                port=config.PORT,
                reload=True)