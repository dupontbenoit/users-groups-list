import csv
from django.core.management.base import BaseCommand
from ug.models import User, Group


class Command(BaseCommand):
    help = 'Loading of new users and groups'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        with open(options['csv_file'], "rt", encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                if self.is_user(row[0]):
                    self.create_or_update_user(row)

    def is_user(self, value: str):
        return value == 'U'

    def is_group(self, value: str):
        return value == 'G'

    def create_or_update_user(self, row):
        obj, created, = User.objects.update_or_create(
            email_address=row[1], defaults={'display_name': row[2]}
        )
