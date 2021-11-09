from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=254, unique=True)
    parent = models.ManyToManyField("self", blank=True)

    def __str__(self) -> str:
        return self.name


class User(models.Model):
    email_address = models.EmailField(unique=True)
    display_name = models.CharField(max_length=254)
    groups = models.ManyToManyField(Group)

    def __str__(self) -> str:
        return self.display_name
