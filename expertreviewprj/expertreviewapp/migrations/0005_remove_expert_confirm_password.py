# Generated by Django 4.1.5 on 2023-03-28 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expertreviewapp', '0004_expert_date_expert_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expert',
            name='confirm_password',
        ),
    ]