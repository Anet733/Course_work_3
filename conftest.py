import pytest


@pytest.fixture
def test_data():
    return [
        {
            "id": 509645757,
            "state": "CANCELED",
            "date": "2017-10-30T01:49:52.939296",
            "operationAmount": {
                "amount": "23036.03",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Gold 7756673469642839",
            "to": "Счет 48943806953649539453"
        },
        {
            "id": 801684332,
            "state": "EXECUTED",
            "date": "2018-11-05T12:04:13.781725",
            "operationAmount": {
                "amount": "21344.35",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 77613226829885488381"
        },
        {
            "id": 122284694,
            "state": "EXECUTED",
            "date": "2019-08-08T21:58:06.688541",
            "operationAmount": {
                "amount": "98657.83",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 99668626339273709694",
            "to": "Счет 27219929444683698245"
        }
        ]

