from conftest import test_data
from src.utils import format_date


def test_main(test_data):
    formatted_list = format_date(test_data)
    assert [i for i in formatted_list] == ['\n'
 '30.10.2017 Перевод с карты на счет\n'
 'Visa Gold 7756 67** **** 2839 -> Счет **9453\n'
 '23036.03 руб.\n'
 '    ',
 '\n05.11.2018 Открытие вклада\n   Счет **8381\n21344.35 руб.\n    ',
 '\n'
 '08.08.2019 Перевод организации\n'
 'Счет **9694 -> Счет **8245\n'
 '98657.83 руб.\n'
 '    ']