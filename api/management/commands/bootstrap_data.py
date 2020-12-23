from django.core.management.base import BaseCommand
from api.models import Shoe, ShoeColor, ShoeType


class Command(BaseCommand):
    help = 'Add data to api'

    def add_arguments(self, parser):
        parser.add_argument('data', type=int)

    def handle(self, *args, **options):
        data = options.get('data')
        count = ShoeType.objects.all().count()
        multiply = count * data
        print(multiply)

