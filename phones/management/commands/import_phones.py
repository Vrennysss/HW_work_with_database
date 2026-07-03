
import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from phones.models import Phone

class Command(BaseCommand):
    help = 'Импорт телефонов из CSV-файла'

    def handle(self, *args, **options):
        csv_path = 'phones.csv'

        Phone.objects.all().delete()

        with open(csv_path, encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                price = row['price'].replace(',', '.')
                release_date = datetime.strptime(row['release_date'], '%Y-%m-%d').date()
                lte_exists = row['lte_exists'].strip().lower() in ('true', '1', 'yes')

                phone = Phone(
                    name=row['name'],
                    price=price,
                    image=row['image'],
                    release_date=release_date,
                    lte_exists=lte_exists,
                )
                phone.save()

        self.stdout.write(self.style.SUCCESS('Импорт завершён'))