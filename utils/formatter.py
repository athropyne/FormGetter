from typing import Any

from utils.walidator import IValidator


class Formatter:
    @staticmethod
    async def sort_by_type(pattern: dict, mask: list | None = None):
        _mask = mask
        if mask is None:
            _mask = ["date", "phone", "email", "text"]
        if len(_mask) != len(set(_mask)):
            raise ValueError("типы данных не могут повторяться!")

        sorted_pattern = {}
        for i in _mask:
            for k, v in pattern.items():
                if i == v:
                    sorted_pattern[k] = v

        # for k, v in pattern.items():
        #     if v == "date":
        #         sorted_pattern[k] = v
        #         continue
        #     if v == "phone":
        #         sorted_pattern[k] = v
        #         continue
        #     if v == "email":
        #         sorted_pattern[k] = v
        #         continue
        #     if v == "text":
        #         sorted_pattern[k] = v
        #         continue
        return sorted_pattern

    @staticmethod
    async def format(data: dict, validators: list[IValidator]):
        formatted_data = {key: "text" for key, _ in data.items()}
        for key, value in data.items():
            for validator in validators:
                if await validator.validate(value):
                    formatted_data[key] = validator.__class__.__name__.replace("Validator", '').lower()

        return await Formatter.sort_by_type(formatted_data)
