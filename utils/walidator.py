import datetime
import re
from enum import Enum


class FieldTypes(str, Enum):
    DATE = "date"
    PHONE = "phone"
    EMAIL = "email"
    TEXT = "text"


class Validator:
    @staticmethod
    async def __date_v1_validator(value: str):
        format_v1 = "%d.%m.%Y"
        try:
            datetime.datetime.strptime(value, format_v1)
            return True
        except ValueError:
            return False

    @staticmethod
    async def __date_v2_validator(value: str):
        format_v2 = "%Y-%m-%d"
        try:
            datetime.datetime.strptime(value, format_v2)
            return True
        except ValueError:
            return False

    @staticmethod
    async def __phone_validator(value: str):
        phone = re.compile(r'^\+\d(\s\d{3}){2}(\s\d{2}){2}$')
        if phone.match(value):
            return True
        return False

    @staticmethod
    async def __email_validator(value: str):
        email = re.compile(r'^[a-zA-Z\d]+([.-][a-zA-Z\d]+)*@[a-zA-Z\d]+(-[a-zA-Z\d]+)*\.[a-zA-Z]+$')
        if email.match(value):
            return True
        return False

    @staticmethod
    async def type_validator(value: str):
        """вот так я обычно не делаю, не то что программа будет масштабироваться не планируется ))"""
        if await Validator.__date_v1_validator(value) or await Validator.__date_v2_validator(value):
            return FieldTypes.DATE
        elif await Validator.__phone_validator(value):
            return FieldTypes.PHONE
        elif await Validator.__email_validator(value):
            return FieldTypes.EMAIL
        else:
            return FieldTypes.TEXT



