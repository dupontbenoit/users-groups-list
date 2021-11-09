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
                    user, created = self.create_or_update_user(row)
                    self.handle_user_groups(user, row)

                if self.is_group(row[0]):
                    group, created = self.create_or_update_group(row[1])
                    self.handle_groups_of_group(group, row)

    def is_user(self, value: str):
        return value == 'U'

    def is_group(self, value: str):
        return value == 'G'

    def create_or_update_user(self, row):
        obj, created = User.objects.update_or_create(
            email_address=row[1], defaults={'display_name': row[2]}
        )
        return (obj, created)

    def create_or_update_group(self, group_name):
        obj, created = Group.objects.update_or_create(
            name=group_name
        )
        return (obj, created)

    def handle_user_groups(self, user: User, row):
        if len(row) > 3:
            for group in row[3].split(';'):
                saved_group, created = self.create_or_update_group(group)
                user.groups.add(saved_group)
            user.save()

    def handle_groups_of_group(self, group: Group, row):
        if len(row) > 2:
            for group_name in row[2].split(';'):
                parent_group, created = Group.objects.get_or_create(name=group_name)
                print('----')
                print(parent_group)
                print('---')
                group.parent.add(parent_group)
            group.save()
