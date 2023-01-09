from requests import post

from core import config
from tests.data import FakeData


def fake_client(request_body: dict):
    url = f"http://{config.HOST}:{config.PORT}/get_form"
    response = post(url=url, data=request_body)
    return response.text


def action_test(_data: list[dict]):
    [
        print(f"QUERY: {i} \nRESULT: {fake_client(i)}\n\n")
        for i in _data
    ]


if __name__ == "__main__":
    data = FakeData.get_all_fake_data__()
    action_test(data)
