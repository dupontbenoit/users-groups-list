import csv
from django.core.management.base import BaseCommand
from ug.models import User, Group
from ug.services.import_service import CsvImport


class Command(BaseCommand):
    help = 'Loading of new users and groups'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csvImportService = CsvImport()
        csvImportService.load(options['csv_file'])
