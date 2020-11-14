# Generated by Django 3.1.2 on 2020-11-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='General_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Inspection_type', models.CharField(max_length=30)),
                ('booking_ref_number', models.CharField(max_length=100)),
                ('supplier_info', models.TextField(max_length=200)),
                ('inspection_date', models.DateField()),
                ('shipment_date', models.DateField()),
            ],
        ),
    ]
