# Generated by Django 4.0.5 on 2022-07-09 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_booking_u_duration_alter_booking_u_timeslot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='U_status',
            field=models.BooleanField(default=False),
        ),
    ]
