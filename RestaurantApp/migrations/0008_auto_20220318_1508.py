# Generated by Django 3.1.4 on 2022-03-18 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApp', '0007_auto_20211125_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery',
            old_name='speed_of_the_bot',
            new_name='speed',
        ),
    ]
