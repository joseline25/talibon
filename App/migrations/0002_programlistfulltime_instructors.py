# Generated by Django 4.0.4 on 2022-08-02 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programlistfulltime',
            name='instructors',
            field=models.ManyToManyField(blank=True, related_name='programs', through='App.InstructorFullTime', to='App.instructor'),
        ),
    ]
