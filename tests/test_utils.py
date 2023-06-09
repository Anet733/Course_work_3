from src.utils import *


def test_sort_dict(test_data):
    sorted_data = sort_dict(test_data)
    assert [x['date'] for x in sorted_data] == ['2019-08-08T21:58:06.688541', '2018-11-05T12:04:13.781725', '2017-10-30T01:49:52.939296']


def test_filter_state(test_data):
    filter_data = filter_state(test_data)
    assert [x['state'] for x in filter_data] == ['EXECUTED', 'EXECUTED']


def test_get_info_from_json(test_data):
    assert test_data == [
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


def test_format_date(test_data):
    format_data = format_date(test_data)
    assert format_data == ['\n30.10.2017 Перевод с карты на счет\nVisa Gold 7756 67** **** 2839 -> Счет **9453\n23036.03 руб.\n    ', '\n05.11.2018 Открытие вклада\n   Счет **8381\n21344.35 руб.\n    ', '\n08.08.2019 Перевод организации\nСчет **9694 -> Счет **8245\n98657.83 руб.\n    ']

