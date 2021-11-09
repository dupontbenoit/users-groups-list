from django.db import models


class User(models.Model):
    email_address = models.EmailField(unique=True)
    display_name = models.CharField(max_length=254)


class Group(models.Model):
    name = models.CharField(max_length=254, unique=True)
