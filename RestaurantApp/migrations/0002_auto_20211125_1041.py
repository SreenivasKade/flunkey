# Generated by Django 3.1.4 on 2021-11-25 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='table_no',
            field=models.CharField(max_length=20),
        ),
    ]