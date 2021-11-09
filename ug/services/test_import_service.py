from django.test import TestCase
from ug.services.import_service import CsvImport

class CsvImportTestCase(TestCase):
    def setUp(self) -> None:
        self.import_service = CsvImport()

    def test_is_user(self):
        self.assertTrue(self.import_service.is_user('U'))
        self.assertFalse(self.import_service.is_user('G'))

    def test_is_group(self):
        self.assertTrue(self.import_service.is_group('G'))
        self.assertFalse(self.import_service.is_group('U'))
