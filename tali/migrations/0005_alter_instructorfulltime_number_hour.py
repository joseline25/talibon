# Generated by Django 4.0.4 on 2022-06-25 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tali', '0004_instructorfulltime_programlistfulltime_instructors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructorfulltime',
            name='number_hour',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]