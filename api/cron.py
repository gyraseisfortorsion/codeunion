import requests
import xml.etree.ElementTree as ET
from api.models import Currency
import logging


# logger = logging.getLogger(__name__)
def update_currency_rates():
    url = 'http://www.nationalbank.kz/rss/rates_all.xml'
    response = requests.get(url)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        for item in root.findall('channel/item'):
            name = item.find('title').text
            rate_str = item.find('description').text
            rate = float(rate_str) if rate_str else None
            if rate is not None:
                currency, created = Currency.objects.get_or_create(name=name, defaults={'rate': rate})
                if not created:
                    currency.rate = rate
                    currency.save()
                # logger.info('Currency rates updated successfully.')
                print(f'Currency {name} updated successfully.')
            else:
                # logger.error(f'Failed to retrieve data from {url}')
                print(f'Failed to parse rate for currency {name}.')
    else:
        print(f'Failed to retrieve data from {url}')
