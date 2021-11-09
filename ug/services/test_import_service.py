from django.test import TestCase
from ug.services.import_service import CsvImport
from ug.models import User, Group

class CsvImportTestCase(TestCase):
    def setUp(self) -> None:
        self.import_service = CsvImport()

    def test_is_user(self):
        self.assertTrue(self.import_service.is_user('U'))
        self.assertFalse(self.import_service.is_user('G'))

    def test_is_group(self):
        self.assertTrue(self.import_service.is_group('G'))
        self.assertFalse(self.import_service.is_group('U'))

    def test_create_or_update_user(self):
        user: User = User()
        user.email_address = 'dupont.benoit@gmail.com'
        user.display_name = 'benoit'
        user.save()
        db_user: User = User.objects.get(email_address='dupont.benoit@gmail.com')
        self.assertEqual(user.email_address, db_user.email_address)
