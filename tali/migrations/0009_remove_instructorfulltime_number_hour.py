# Generated by Django 4.0.4 on 2022-06-28 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tali', '0008_alter_instructorfulltime_number_hour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructorfulltime',
            name='number_hour',
        ),
    ]