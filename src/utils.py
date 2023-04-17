import json
from datetime import datetime


def get_info_from_json(file):
    """
    Открываем файл json, имеющийся в условии
    """

    with open(file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def filter_state(data):
    """
    Убирем из списка значенеи без статуса
    """
    data = [x for x in data if 'state' in x and x['state'] == "EXECUTED"]
    return data


def sort_dict(data):
    """
    Сортируем по дате и берем только первые 5 значений
    """
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]


def format_date(data):
    """
    Составляем конечный список в необходимом формате
    """
    formatted_date = []
    for i in data:
        date = datetime.strptime(i['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = i['description']
        if 'from' in i:
            the_arrow = '->'
            sender = i['from'].split()
            sender_bill = sender.pop(-1)
            sender_info = " ".join(sender)
            if len(sender_bill) == 16:
                sender_bill = f'{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}'
            else:
                sender_bill = f'**{sender_bill[-4:]}'
        else:
            sender_info = ""
            sender_bill = ""
            the_arrow = ""
        recipient = i['to'].split()
        recipient_bill = recipient.pop(-1)
        recipient_info = " ".join(recipient)
        if len(recipient_bill) == 16:
            recipient_bill = f'{recipient_bill[:4]} {recipient_bill[4:6]}** **** {recipient_bill[-4:]}'
        else:
            recipient_bill = f'**{recipient_bill[-4:]}'
        total_amount = i['operationAmount']['amount']
        currency = i['operationAmount']['currency']['name']

        formatted_date.append(f"""
{date} {description}
{sender_info} {sender_bill} {the_arrow} {recipient_info} {recipient_bill}
{total_amount} {currency}
    """)
    return formatted_date







