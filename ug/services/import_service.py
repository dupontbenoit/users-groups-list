import csv
from ug.models import User, Group


class CsvImport:
    def __init__(self) -> None:
        pass

    def load(self, file):
        with open(file, "rt", encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                if self.is_user(row[0]):
                    self.create_or_update_user(row)

                if self.is_group(row[0]):
                    self.create_or_update_group(row)

    def is_user(self, value: str):
        return value == 'U'

    def is_group(self, value: str):
        return value == 'G'

    def create_or_update_user(self, row):
        obj, created = User.objects.update_or_create(
            email_address=row[1], defaults={'display_name': row[2]}
        )
        return (obj, created)

    def create_or_update_group(self, row):
        obj, created = Group.objects.update_or_create(
            name=row[1]
        )
        return (obj, created)
