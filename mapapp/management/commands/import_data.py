import csv
from django.core.management.base import BaseCommand
from mapapp.models import OutdoorShelter

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def handle(self, *args, **options):
        csv_file_path = 'C:/Users/kim/Hackathon/parsed_data.csv'  # CSV 파일 경로를 적절히 수정해주세요.

        with open(csv_file_path, 'r', encoding='utf-16') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                OutdoorShelter.objects.create(
                    vt_acmdfclty_nm=row['vt_acmdfclty_nm'],
                    dtl_adres=row['dtl_adres'],
                    xcord=float(row['xcord']),
                    ycord=float(row['ycord'])
                )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
