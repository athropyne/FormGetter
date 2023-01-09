from typing import Type

from utils.walidator import Validator


class Formatter:
    @staticmethod
    async def format(data: dict, validator: Type[Validator]):
        return {key: await validator.type_validator(value) for key, value in data.items()}

