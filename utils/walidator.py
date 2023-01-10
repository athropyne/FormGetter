import datetime
import re
from abc import ABC, abstractmethod


class IValidator(ABC):
    @abstractmethod
    async def validate(self, value: str) -> bool:
        pass


class DateValidator(IValidator):
    def __init__(self):
        self.flag = None

    async def validate(self, value: str) -> bool:
        self.flag: bool = False
        data_format = ["%d.%m.%Y", "%Y-%m-%d"]

        for df in data_format:
            try:
                datetime.datetime.strptime(value, df)
                self.flag = True
            except ValueError:
                continue
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
