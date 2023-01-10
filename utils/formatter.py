from utils.walidator import IValidator


class Formatter:
    @staticmethod
    async def format(data: dict, validators: list[IValidator]):
        formatted_data = {key: "text" for key, _ in data.items()}
        for key, value in data.items():
            for validator in validators:
                if await validator.validate(value):
                    formatted_data[key] = validator.__class__.__name__.replace("Validator", '').lower()

        return formatted_data
