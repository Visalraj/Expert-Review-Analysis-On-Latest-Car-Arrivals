# Generated by Django 4.1.5 on 2023-02-24 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expertreviewapp', '0002_remove_registration_address_registration_addressone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='dob',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='gender',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
