# Generated by Django 4.1.5 on 2023-02-25 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expertreviewapp', '0006_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]