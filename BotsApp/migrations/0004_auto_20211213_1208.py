# Generated by Django 3.1.4 on 2021-12-13 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BotsApp', '0003_auto_20211125_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='bot_name',
            field=models.CharField(max_length=300),
        ),
    ]
