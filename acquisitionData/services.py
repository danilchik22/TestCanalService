from datetime import datetime

import httplib2
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials
import xml.etree.ElementTree as et
import requests
from .models import Order

def update_database():
    CREDENTIALS_FILE = 'creds.json'
    spreadsheets_id = '1A1tm40no_4LphRAkKfqahUH5OhVOf8YdNhuy5ilTKjQ'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = discovery.build('sheets', 'v4', http = httpAuth)

    dict_values = service.spreadsheets().values().get(
        spreadsheetId = spreadsheets_id,
        range='A:D',
        majorDimension='ROWS'
    ).execute()
    lst_values = dict_values['values']
    lst_clear_values = lst_values[1:]
    add_into_base(lst_clear_values)


def add_into_base(lst_orders):
    course_str = get_course('R01235')
    course = float(course_str.replace(',', '.'))
    for order in lst_orders:
        id = int(order[0])
        number = int(order[1])
        price_dollar = float(order[2])
        date = convert_str_into_datetime(order[3])
        price_rub = round(course * price_dollar, 2)
        Order.objects.update_or_create(pk=id, number_order=number, price=price_dollar, date_of_suply=date, price_in_ruble=price_rub)


def convert_str_into_datetime(date_str):
    date_formatter = '%d.%m.%Y'
    date = datetime.strptime(date_str, date_formatter)
    return date

def get_course(id):
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'
    root_node = et.fromstring(requests.get(url).content)
    for tag in root_node.findall('Valute'):
        if tag.get('ID') == id:
            target_tag = tag
            break
    if target_tag:
        result = target_tag.find('Value').text
        return result
    else:
        Exception('Нет такого ID курса')



