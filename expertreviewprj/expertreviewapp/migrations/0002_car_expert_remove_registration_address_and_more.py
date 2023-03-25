# Generated by Django 4.1.5 on 2023-03-23 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expertreviewapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandname', models.CharField(max_length=255, null=True)),
                ('carname', models.CharField(max_length=255, null=True)),
                ('modelname', models.CharField(max_length=200, null=True)),
                ('seats', models.CharField(max_length=255, null=True)),
                ('fuel', models.CharField(max_length=20, null=True)),
                ('price', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('rv', models.CharField(default=0, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=255)),
                ('mobilenumber', models.CharField(max_length=20)),
                ('experience', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=255)),
                ('confirm_password', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='registration',
            name='address',
        ),
        migrations.AddField(
            model_name='registration',
            name='addressone',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='addresstwo',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='c_password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='city',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='district',
            field=models.CharField(max_length=250, null=True),
        ),
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
        migrations.AddField(
            model_name='registration',
            name='pincode',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='state',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='firstname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='lastname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='mobileno',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.CharField(max_length=255, null=True)),
                ('extandint', models.CharField(max_length=200, null=True)),
                ('engine', models.CharField(max_length=255, null=True)),
                ('suspension', models.CharField(max_length=20, null=True)),
                ('electronics', models.CharField(max_length=200, null=True)),
                ('fluids', models.CharField(max_length=255, null=True)),
                ('tires', models.CharField(max_length=255, null=True)),
                ('info', models.CharField(max_length=200, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('statusofreview', models.IntegerField(default=0)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expertreviewapp.car')),
                ('exp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expertreviewapp.expert')),
            ],
        ),
    ]