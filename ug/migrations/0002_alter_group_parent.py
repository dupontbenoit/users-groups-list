# Generated by Django 3.2.9 on 2021-11-09 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ug', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='parent',
            field=models.ManyToManyField(blank=True, to='ug.Group'),
        ),
    ]
