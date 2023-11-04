from django.core.management.base import BaseCommand
from api.models import Currency

class Command(BaseCommand):
    help = 'Update or view currency data'

    def add_arguments(self, parser):
        parser.add_argument('currency_id', type=int, help='Currency ID')
        parser.add_argument('rate', type=float, help='Currency exchange rate')

    def handle(self, *args, **kwargs):
        currency_id = kwargs['currency_id']
        rate = kwargs['rate']

        try:
            currency = Currency.objects.get(id=currency_id)
            currency.rate = rate
            currency.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully updated currency with ID {currency_id}'))
        except Currency.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Currency with ID {currency_id} does not exist'))