# Generated by Django 4.1.5 on 2023-02-25 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expertreviewapp', '0004_cars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='car_id',
        ),
    ]
