# Generated by Django 3.1.4 on 2021-11-25 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BotsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='battery',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]