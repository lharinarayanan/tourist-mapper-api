# Generated by Django 2.1.3 on 2019-01-19 10:02

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('guide_id', models.AutoField(primary_key=True, serialize=False)),
                ('guide_name', models.CharField(max_length=255)),
                ('place_name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
                ('languages_known', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(choices=[(True, 'active'), (False, 'inactive')])),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospital_id', models.AutoField(primary_key=True, serialize=False)),
                ('hospital_name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('zone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=1255)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
                ('ambulance_service', models.BooleanField(choices=[(True, 'available'), (False, 'unavailable')])),
            ],
        ),
        migrations.CreateModel(
            name='ParkingLot',
            fields=[
                ('lot_id', models.AutoField(primary_key=True, serialize=False)),
                ('place_name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('no_of_lots', models.IntegerField()),
                ('slots_occupied', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('place_id', models.AutoField(primary_key=True, serialize=False)),
                ('place_name', models.CharField(max_length=255)),
                ('place_type', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('reviews', models.TextField()),
                ('services_provided', models.TextField()),
                ('crowd_density', models.FloatField()),
                ('website_url', models.TextField()),
                ('additional_info', models.TextField()),
                ('photo_link', models.URLField()),
                ('is_available', models.BooleanField(choices=[(True, 'available'), (False, 'unavailable')])),
            ],
        ),
        migrations.CreateModel(
            name='PoliceStation',
            fields=[
                ('station_id', models.AutoField(primary_key=True, serialize=False)),
                ('station_name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('zone', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
                ('address', models.CharField(max_length=1255)),
            ],
        ),
        migrations.CreateModel(
            name='Road',
            fields=[
                ('road_id', models.AutoField(primary_key=True, serialize=False)),
                ('road_name', models.CharField(max_length=255)),
                ('condition', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('volunteer_id', models.AutoField(primary_key=True, serialize=False)),
                ('road_name', models.CharField(max_length=999)),
                ('volunteer_name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
                ('is_present', models.BooleanField(choices=[(True, 'available'), (False, 'unavailable')])),
            ],
        ),
    ]