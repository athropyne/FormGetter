import datetime
import re
from abc import ABC, abstractmethod
from enum import Enum


class IValidator(ABC):
    @abstractmethod
    async def validate(self, value: str) -> bool:
        pass


class DateValidator(IValidator):
    def __init__(self):
        self.flag = None

    async def validate(self, value: str) -> bool:
        self.flag: bool = False
        format_v2 = "%Y-%m-%d"
        format_v1 = "%d.%m.%Y"
        try:
            datetime.datetime.strptime(value, format_v2)
            self.flag = True
        except ValueError:
            self.flag = False
        try:
            datetime.datetime.strptime(value, format_v1)
            self.flag = True
        except ValueError:
            self.flag = False

        return self.flag


class PhoneValidator(IValidator):
    async def validate(self, value: str) -> bool:
        phone = re.compile(r'^\+\d(\s\d{3}){2}(\s\d{2}){2}$')
        if phone.match(value):
            return True
        return False


class EmailValidator(IValidator):
    async def validate(self, value: str) -> bool:
        email = re.compile(r'^[a-zA-Z\d]+([.-][a-zA-Z\d]+)*@[a-zA-Z\d]+(-[a-zA-Z\d]+)*\.[a-zA-Z]+$')
        if email.match(value):
            return True
        return False

