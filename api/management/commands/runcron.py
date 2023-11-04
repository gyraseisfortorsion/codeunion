from django.core.management.base import BaseCommand
from api.cron import update_currency_rates

class Command(BaseCommand):
    help = 'Runs the currency update CRON job'

    def handle(self, *args, **options):
        update_currency_rates()