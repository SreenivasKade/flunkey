# Generated by Django 3.1.4 on 2022-03-04 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exit',
            name='value',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)]),
        ),
    ]
