# Generated by Django 3.2.3 on 2021-05-26 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_patient_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='profile_pic',
        ),
    ]
