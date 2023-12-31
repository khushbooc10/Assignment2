# Generated by Django 4.2.3 on 2023-07-11 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('prescription_details', models.TextField()),
            ],
        ),
    ]
